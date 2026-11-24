const fs = require('fs');

const domainsData = JSON.parse(fs.readFileSync('database-docs/source/domains.json', 'utf8')).domains;
const tablesData = JSON.parse(fs.readFileSync('database-docs/source/tables.json', 'utf8')).data;
const relationshipsData = JSON.parse(fs.readFileSync('database-docs/source/relationships.json', 'utf8')).data;

const tableRowCounts = {};
for (const t of tablesData) {
  tableRowCounts[`${t.table_schema}.${t.table_name}`] = t.estimated_row_count;
}

const COMPACT_WIDTH = 260;
const COMPACT_HEIGHT = 44;

const DOMAIN_KEYS = Object.keys(domainsData);
const GRID_COLS = 3;
const CONTAINER_WIDTH = 1200;
const CONTAINER_GAP_X = 140;
const CONTAINER_GAP_Y = 140;

const domainLayouts = {};
let currentY = [180, 180, 180];

DOMAIN_KEYS.forEach((dKey, idx) => {
  const colIdx = idx % GRID_COLS;
  const domain = domainsData[dKey];
  const tables = domain.tables;
  
  const subCols = 3;
  const subRows = Math.ceil(tables.length / subCols);
  const containerHeight = 80 + (subRows * (COMPACT_HEIGHT + 12)) + 30;
  
  const containerX = 140 + colIdx * (CONTAINER_WIDTH + CONTAINER_GAP_X);
  const containerY = currentY[colIdx];
  currentY[colIdx] += containerHeight + CONTAINER_GAP_Y;
  
  const tablePositions = {};
  tables.forEach((tName, tIdx) => {
    const sCol = tIdx % subCols;
    const sRow = Math.floor(tIdx / subCols);
    const tx = containerX + 30 + sCol * (COMPACT_WIDTH + 24);
    const ty = containerY + 65 + sRow * (COMPACT_HEIGHT + 12);
    tablePositions[`public.${tName}`] = {
      x: tx,
      y: ty,
      width: COMPACT_WIDTH,
      height: COMPACT_HEIGHT,
      rowCount: tableRowCounts[`public.${tName}`] || 0
    };
  });
  
  domainLayouts[dKey] = {
    domainKey: dKey,
    displayName: domain.display_name,
    description: domain.description,
    x: containerX,
    y: containerY,
    width: CONTAINER_WIDTH,
    height: containerHeight,
    tables: tablePositions
  };
});

// External schemas container
const extColIdx = 2;
const extX = 140 + extColIdx * (CONTAINER_WIDTH + CONTAINER_GAP_X);
const extY = currentY[extColIdx];
const extTables = [
  "auth.users", "auth.identities", "auth.sessions",
  "storage.buckets", "storage.objects",
  "cron.job", "cron.job_run_details",
  "net.http_request", "net._http_response",
  "vault.secrets", "vault.decrypted_secrets"
];
const extSubRows = Math.ceil(extTables.length / 3);
const extHeight = 80 + (extSubRows * (COMPACT_HEIGHT + 12)) + 30;
const extPositions = {};
extTables.forEach((tName, tIdx) => {
  const sCol = tIdx % 3;
  const sRow = Math.floor(tIdx / 3);
  extPositions[tName] = {
    x: extX + 30 + sCol * (COMPACT_WIDTH + 24),
    y: extY + 65 + sRow * (COMPACT_HEIGHT + 12),
    width: COMPACT_WIDTH,
    height: COMPACT_HEIGHT,
    rowCount: 0
  };
});

domainLayouts["external_infrastructure"] = {
  domainKey: "external_infrastructure",
  displayName: "Supabase Platform & Extensions Infrastructure",
  description: "External auth, storage, pg_cron, pg_net, and vault schemas managed by Supabase platform.",
  x: extX,
  y: extY,
  width: CONTAINER_WIDTH,
  height: extHeight,
  tables: extPositions
};
currentY[extColIdx] += extHeight + CONTAINER_GAP_Y;

const totalCanvasW = 140 + 3 * (CONTAINER_WIDTH + CONTAINER_GAP_X) + 100;
const totalCanvasH = Math.max(...currentY) + 200;

const allTableCoords = {};
Object.values(domainLayouts).forEach(d => {
  Object.entries(d.tables).forEach(([tKey, pos]) => {
    allTableCoords[tKey] = pos;
  });
});

const masterEdges = [];
relationshipsData.forEach((fk, idx) => {
  const srcKey = `${fk.source_schema}.${fk.source_table}`;
  const tgtKey = `${fk.target_schema}.${fk.target_table}`;
  if (allTableCoords[srcKey] && allTableCoords[tgtKey]) {
    const s = allTableCoords[srcKey];
    const t = allTableCoords[tgtKey];
    masterEdges.push({
      id: `mfk_${idx}`,
      constraint_name: fk.constraint_name,
      source: srcKey,
      target: tgtKey,
      source_col: fk.source_column,
      target_col: fk.target_column,
      delete_rule: fk.delete_action,
      start: { x: s.x + s.width, y: s.y + s.height / 2 },
      end: { x: t.x, y: t.y + t.height / 2 }
    });
  }
});

const masterOutput = {
  canvas: {
    width: totalCanvasW,
    height: totalCanvasH
  },
  domains: domainLayouts,
  edges_count: masterEdges.length,
  edges: masterEdges
};

fs.writeFileSync('database-docs/diagrams/layout_master.json', JSON.stringify(masterOutput, null, 2));
console.log(`Saved Master Architecture layout (${totalCanvasW}x${totalCanvasH}) with ${masterEdges.length} relationships.`);
