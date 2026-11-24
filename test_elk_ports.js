const ELK = require('elkjs');
const elk = new ELK();

const graph = {
  id: "root",
  layoutOptions: {
    'elk.algorithm': 'layered',
    'elk.direction': 'RIGHT',
    'elk.spacing.nodeNode': '100',
    'elk.layered.spacing.nodeNodeBetweenLayers': '160',
    'elk.edgeRouting': 'ORTHOGONAL',
    'elk.layered.mergeEdges': 'false'
  },
  children: [
    {
      id: "tbl_members",
      width: 380,
      height: 220,
      ports: [
        { id: "members_p_org_id", x: 380, y: 70, properties: { 'port.side': 'EAST' } },
        { id: "members_p_user_id", x: 380, y: 100, properties: { 'port.side': 'EAST' } }
      ]
    },
    {
      id: "tbl_orgs",
      width: 380,
      height: 420,
      ports: [
        { id: "orgs_p_id", x: 0, y: 40, properties: { 'port.side': 'WEST' } }
      ]
    }
  ],
  edges: [
    {
      id: "e1",
      sources: ["members_p_org_id"],
      targets: ["orgs_p_id"]
    }
  ]
};

elk.layout(graph)
  .then(res => {
    console.log("ELK with Ports Result:");
    console.log("Edge e1:", JSON.stringify(res.edges[0]));
  })
  .catch(console.error);
