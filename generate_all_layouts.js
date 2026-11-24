const fs = require('fs');
const ELK = require('elkjs');
const elk = new ELK();

// Load metadata
const tablesData = JSON.parse(fs.readFileSync('database-docs/source/tables.json', 'utf8')).data;
const columnsData = JSON.parse(fs.readFileSync('database-docs/source/columns.json', 'utf8')).data;
const relationshipsData = JSON.parse(fs.readFileSync('database-docs/source/relationships.json', 'utf8')).data;
const constraintsData = JSON.parse(fs.readFileSync('database-docs/source/constraints.json', 'utf8')).data;
const domainsData = JSON.parse(fs.readFileSync('database-docs/source/domains.json', 'utf8')).domains;

// Group columns
const colsByTable = {};
for (const col of columnsData) {
  const key = `${col.table_schema}.${col.table_name}`;
  if (!colsByTable[key]) colsByTable[key] = [];
  colsByTable[key].push(col);
}

// Synthetic external tables
colsByTable['auth.users'] = [
  { table_schema: 'auth', table_name: 'users', column_name: 'id', data_type: 'uuid', is_nullable: 'NO', column_default: 'gen_random_uuid()' },
  { table_schema: 'auth', table_name: 'users', column_name: 'email', data_type: 'text', is_nullable: 'YES', column_default: null },
  { table_schema: 'auth', table_name: 'users', column_name: 'created_at', data_type: 'timestamp with time zone', is_nullable: 'NO', column_default: 'now()' }
];
colsByTable['public.organizations'] = colsByTable['public.organizations'] || [];

const TABLE_WIDTH = 440;
const HEADER_HEIGHT = 44;
const ROW_HEIGHT = 26;
const PADDING_BOTTOM = 12;

async function computeDomainLayout(domainKey, tableList, externalReferences = [], layoutFileName) {
  console.log(`\nComputing layout for [${domainKey}] with ${tableList.length} tables + ${externalReferences.length} refs...`);
  const allTables = [...tableList.map(t => `public.${t}`), ...externalReferences];
  
  const elkNodes = [];
  const tableLayoutMeta = {};

  for (const fullTableName of allTables) {
    const cols = colsByTable[fullTableName] || [];
    const height = HEADER_HEIGHT + (cols.length * ROW_HEIGHT) + PADDING_BOTTOM;

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
      ports.push({
        id: `${fullTableName}_in_${col.column_name}`,
        x: 0,
        y: yOffset,
        properties: { 'port.side': 'WEST' }
      });
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

  // Find relationships within this scope
  const scopedFks = [];
  for (const fk of relationshipsData) {
    const srcKey = `${fk.source_schema}.${fk.source_table}`;
    const tgtKey = `${fk.target_schema}.${fk.target_table}`;
    if (allTables.includes(srcKey) && allTables.includes(tgtKey)) {
      scopedFks.push(fk);
    }
  }

  console.log(`  Found ${scopedFks.length} foreign keys within domain scope.`);

  const elkEdges = scopedFks.map((fk, idx) => {
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

  const res = await elk.layout(elkGraph);

  let maxX = 0;
  let maxY = 0;
  for (const c of res.children) {
    if (c.x + c.width > maxX) maxX = c.x + c.width;
    if (c.y + c.height > maxY) maxY = c.y + c.height;
  }

  const canvasWidth = Math.max(maxX + 300, 3200);
  const canvasHeight = Math.max(maxY + 300, 2400);

  const outputData = {
    domainKey,
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

  fs.writeFileSync(`database-docs/diagrams/${layoutFileName}`, JSON.stringify(outputData, null, 2));
  console.log(`  Saved layout to database-docs/diagrams/${layoutFileName} (${canvasWidth}x${canvasHeight})`);
}

async function runAllLayouts() {
  // 1. Campaigns & Email Delivery Pipeline (18 tables)
  const campTables = [
    ...domainsData.campaigns_and_templates.tables,
    ...domainsData.email_delivery_and_ses.tables
  ];
  await computeDomainLayout("campaigns_and_delivery", campTables, ["public.organizations"], "layout_campaigns_delivery.json");

  // 2. Inbound Email, Mailboxes & Automations (15 tables)
  const autoTables = [
    ...domainsData.mailboxes_and_inbound.tables,
    ...domainsData.automation_and_events.tables
  ];
  await computeDomainLayout("inbound_and_automations", autoTables, ["public.organizations", "public.emails"], "layout_inbound_automations.json");

  // 3. Billing, Subscriptions & Ledgers (20 tables)
  const billingTables = domainsData.billing_and_subscriptions.tables;
  await computeDomainLayout("billing_and_subscriptions", billingTables, ["public.organizations"], "layout_billing.json");

  // 4. Developer API, Webhooks & OAuth (10 tables)
  const devTables = domainsData.developer_api_and_oauth.tables;
  await computeDomainLayout("developer_api_and_oauth", devTables, ["public.organizations", "auth.users"], "layout_developer_api.json");

  // 5. Growth, Lifecycle, Admin & Support (24 tables)
  const opsTables = [
    ...domainsData.growth_referrals_and_blog.tables,
    ...domainsData.lifecycle_and_notifications.tables,
    ...domainsData.admin_support_and_logging.tables
  ];
  await computeDomainLayout("growth_lifecycle_and_admin", opsTables, ["public.organizations", "auth.users"], "layout_growth_lifecycle_admin.json");

  console.log("\nAll domain layouts generated successfully!");
}

runAllLayouts().catch(console.error);
