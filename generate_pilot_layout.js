const fs = require('fs');
const ELK = require('elkjs');
const elk = new ELK();

// 1. Load metadata
const tablesData = JSON.parse(fs.readFileSync('database-docs/source/tables.json', 'utf8')).data;
const columnsData = JSON.parse(fs.readFileSync('database-docs/source/columns.json', 'utf8')).data;
const relationshipsData = JSON.parse(fs.readFileSync('database-docs/source/relationships.json', 'utf8')).data;
const constraintsData = JSON.parse(fs.readFileSync('database-docs/source/constraints.json', 'utf8')).data;
const domainsData = JSON.parse(fs.readFileSync('database-docs/source/domains.json', 'utf8')).domains;

// Pilot tables
const tenancyTables = domainsData.tenancy_and_users.tables;
const crmTables = domainsData.contacts_and_crm.tables;
const pilotTableNames = new Set([...tenancyTables, ...crmTables]);

console.log(`Loaded ${tenancyTables.length} Tenancy tables and ${crmTables.length} CRM tables.`);

// Group columns by table
const colsByTable = {};
for (const col of columnsData) {
  const key = `${col.table_schema}.${col.table_name}`;
  if (!colsByTable[key]) colsByTable[key] = [];
  colsByTable[key].push(col);
}

// Add synthetic auth.users table for FK targets
colsByTable['auth.users'] = [
  { table_schema: 'auth', table_name: 'users', column_name: 'id', data_type: 'uuid', is_nullable: 'NO', column_default: 'gen_random_uuid()' },
  { table_schema: 'auth', table_name: 'users', column_name: 'email', data_type: 'text', is_nullable: 'YES', column_default: null },
  { table_schema: 'auth', table_name: 'users', column_name: 'created_at', data_type: 'timestamp with time zone', is_nullable: 'NO', column_default: 'now()' }
];

// Constraints indexing (PK, UQ)
const pksByTable = {};
const uqsByTable = {};
for (const con of constraintsData) {
  const key = `${con.schema_name}.${con.table_name}`;
  if (con.constraint_type === 'p') {
    if (!pksByTable[key]) pksByTable[key] = new Set();
    // parse column name from definition e.g. PRIMARY KEY (id)
    const m = con.constraint_definition.match(/\((.*?)\)/);
    if (m) {
      m[1].split(',').forEach(c => pksByTable[key].add(c.trim().replace(/"/g, '')));
    }
  } else if (con.constraint_type === 'u') {
    if (!uqsByTable[key]) uqsByTable[key] = new Set();
    const m = con.constraint_definition.match(/\((.*?)\)/);
    if (m) {
      m[1].split(',').forEach(c => uqsByTable[key].add(c.trim().replace(/"/g, '')));
    }
  }
}
pksByTable['auth.users'] = new Set(['id']);

// Table dimensions calculation
const TABLE_WIDTH = 440;
const HEADER_HEIGHT = 44;
const ROW_HEIGHT = 26;
const PADDING_BOTTOM = 12;

const allTablesInPilot = [...pilotTableNames.values()].map(t => `public.${t}`);
allTablesInPilot.push('auth.users');

const elkNodes = [];
const tableLayoutMeta = {};

for (const fullTableName of allTablesInPilot) {
  const cols = colsByTable[fullTableName] || [];
  const colCount = cols.length;
  const height = HEADER_HEIGHT + (colCount * ROW_HEIGHT) + PADDING_BOTTOM;

  tableLayoutMeta[fullTableName] = {
    fullTableName,
    cols,
    width: TABLE_WIDTH,
    height,
    colYOffsets: {}
  };

  const ports = [];
  cols.forEach((col, idx) => {
    const yOffset = HEADER_HEIGHT + (idx * ROW_HEIGHT) + (ROW_HEIGHT / 2);
    tableLayoutMeta[fullTableName].colYOffsets[col.column_name] = yOffset;

    // West port (incoming)
    ports.push({
      id: `${fullTableName}_in_${col.column_name}`,
      x: 0,
      y: yOffset,
      properties: { 'port.side': 'WEST' }
    });
    // East port (outgoing)
    ports.push({
      id: `${fullTableName}_out_${col.column_name}`,
      x: TABLE_WIDTH,
      y: yOffset,
      properties: { 'port.side': 'EAST' }
    });
  });

  elkNodes.push({
    id: fullTableName,
    width: TABLE_WIDTH,
    height: height,
    ports: ports
  });
}

// Foreign keys in pilot
const pilotFks = [];
for (const fk of relationshipsData) {
  const srcKey = `${fk.source_schema}.${fk.source_table}`;
  const tgtKey = `${fk.target_schema}.${fk.target_table}`;
  if (allTablesInPilot.includes(srcKey) && allTablesInPilot.includes(tgtKey)) {
    pilotFks.push(fk);
  }
}

console.log(`Found ${pilotFks.length} foreign keys within pilot scope.`);

const elkEdges = pilotFks.map((fk, idx) => {
  const srcKey = `${fk.source_schema}.${fk.source_table}`;
  const tgtKey = `${fk.target_schema}.${fk.target_table}`;
  return {
    id: `fk_${idx}_${fk.constraint_name}`,
    sources: [`${srcKey}_out_${fk.source_column}`],
    targets: [`${tgtKey}_in_${fk.target_column}`],
    meta: fk
  };
});

const elkGraph = {
  id: "root",
  layoutOptions: {
    'elk.algorithm': 'layered',
    'elk.direction': 'RIGHT',
    'elk.spacing.nodeNode': '100',
    'elk.layered.spacing.nodeNodeBetweenLayers': '180',
    'elk.edgeRouting': 'ORTHOGONAL',
    'elk.layered.mergeEdges': 'false',
    'elk.layered.nodePlacement.strategy': 'BRANDES_KOEPF',
    'elk.layered.crossingMinimization.strategy': 'LAYER_SWEEP'
  },
  children: elkNodes,
  edges: elkEdges
};

console.log("Running ELK graph layout calculation...");

elk.layout(elkGraph)
  .then(res => {
    console.log("ELK layout completed successfully!");

    // Compute bounding canvas
    let maxX = 0;
    let maxY = 0;
    for (const c of res.children) {
      if (c.x + c.width > maxX) maxX = c.x + c.width;
      if (c.y + c.height > maxY) maxY = c.y + c.height;
    }

    const canvasWidth = Math.max(maxX + 300, 3200);
    const canvasHeight = Math.max(maxY + 300, 2400);

    const outputData = {
      canvas: {
        width: canvasWidth,
        height: canvasHeight,
        margin: 120
      },
      nodes: res.children.map(c => ({
        id: c.id,
        x: c.x + 120,
        y: c.y + 160,
        width: c.width,
        height: c.height,
        meta: tableLayoutMeta[c.id]
      })),
      edges: res.edges.map(e => ({
        id: e.id,
        meta: e.meta,
        sections: e.sections.map(s => ({
          startPoint: { x: s.startPoint.x + 120, y: s.startPoint.y + 160 },
          endPoint: { x: s.endPoint.x + 120, y: s.endPoint.y + 160 },
          bendPoints: (s.bendPoints || []).map(b => ({ x: b.x + 120, y: b.y + 160 }))
        }))
      }))
    };

    fs.writeFileSync('database-docs/diagrams/pilot_layout.json', JSON.stringify(outputData, null, 2));
    console.log(`Saved pilot layout to database-docs/diagrams/pilot_layout.json. Canvas size: ${canvasWidth} x ${canvasHeight}`);
  })
  .catch(err => {
    console.error("ELK error:", err);
  });
