"""
A graph in mathematics and computer science consists of "nodes" which may or may not be connected with one another.
Connections between nodes are called edges. A graph can be directed (arrow) or undirected. The edge can represent distance or weight.

Python does not have a graph data type. To use graphs we can either use a module or implement it ourselves:
1. Implement graphs ourselves
2. Networkx module
"""

print("Example #1: Implement graphs ourselves")

graph = {'A': ['B', 'C'],
         'B': ['C', 'A'],
         'C': ['D'],
         'D': ['A']}

print(graph)

print("\nExample #2: Networkx module")

# Install the networkx module using: pip install networkx
# You will need to install virtualenv on OSX otherwise you will have trouble installing networkx module.
import networkx as nx

G = nx.Graph()
G.add_node("A")
G.add_node("B")
G.add_node("C")
G.add_edge("A","B")
G.add_edge("B","C")
G.add_edge("C","A")

print("Nodes: " + str(G.nodes()))
print("Edges: " + str(G.edges()))



