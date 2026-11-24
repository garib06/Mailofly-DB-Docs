const ELK = require('elkjs');
const elk = new ELK();

const graph = {
  id: "root",
  layoutOptions: {
    'elk.algorithm': 'layered',
    'elk.direction': 'RIGHT',
    'elk.spacing.nodeNode': '100',
    'elk.layered.spacing.nodeNodeBetweenLayers': '160',
    'elk.edgeRouting': 'ORTHOGONAL'
  },
  children: [
    { id: "tbl_orgs", width: 380, height: 420 },
    { id: "tbl_users", width: 380, height: 600 },
    { id: "tbl_members", width: 380, height: 220 },
    { id: "tbl_contacts", width: 380, height: 450 }
  ],
  edges: [
    { id: "e1", sources: ["tbl_members"], targets: ["tbl_orgs"] },
    { id: "e2", sources: ["tbl_members"], targets: ["tbl_users"] },
    { id: "e3", sources: ["tbl_contacts"], targets: ["tbl_orgs"] },
    { id: "e4", sources: ["tbl_users"], targets: ["tbl_orgs"] }
  ]
};

elk.layout(graph)
  .then(res => {
    console.log("ELK Placed Children:");
    for (const c of res.children) {
      console.log(`  ${c.id}: x=${c.x}, y=${c.y}, w=${c.width}, h=${c.height}`);
    }
    console.log("\nELK Edges:");
    for (const e of res.edges) {
      console.log(`  ${e.id}: sections=${JSON.stringify(e.sections)}`);
    }
  })
  .catch(console.error);
