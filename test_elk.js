const ELK = require('elkjs');
const elk = new ELK();

const graph = {
  id: "root",
  layoutOptions: {
    'elk.algorithm': 'layered',
    'elk.direction': 'RIGHT',
    'elk.spacing.nodeNode': '80',
    'elk.layered.spacing.nodeNodeBetweenLayers': '120',
    'elk.edgeRouting': 'ORTHOGONAL'
  },
  children: [
    { id: "n1", width: 340, height: 250 },
    { id: "n2", width: 340, height: 400 }
  ],
  edges: [
    { id: "e1", sources: ["n1"], targets: ["n2"] }
  ]
};

elk.layout(graph)
  .then(res => {
    console.log("ELK Layout successful:");
    console.log("n1:", res.children[0].x, res.children[0].y, res.children[0].width, res.children[0].height);
    console.log("n2:", res.children[1].x, res.children[1].y, res.children[1].width, res.children[1].height);
    console.log("edges:", JSON.stringify(res.edges));
  })
  .catch(console.error);
