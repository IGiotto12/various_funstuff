from pyvis.network import Network
import networkx as nx

g = Network(height=800, width=800, notebook=True)
g.toggle_hide_edges_on_drag(False)
g.toggle_physics(True)

for i in range(1, 11):
    g.add_node(i, label=f"Node {i}")

g.show("graph.html")