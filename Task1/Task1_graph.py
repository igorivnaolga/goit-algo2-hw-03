import networkx as nx
import matplotlib.pyplot as plt

# Create a graph
G = nx.DiGraph()

# Add edges with capacity
edges = [
    ("Terminal 1", "Warehouse 1", 25),
    ("Terminal 1", "Warehouse 2", 20),
    ("Terminal 1", "Warehouse 3", 15),
    ("Terminal 2", "Warehouse 3", 15),
    ("Terminal 2", "Warehouse 4", 30),
    ("Terminal 2", "Warehouse 2", 10),
    ("Warehouse 1", "Shop 1", 15),
    ("Warehouse 1", "Shop 2", 10),
    ("Warehouse 1", "Shop 3", 20),
    ("Warehouse 2", "Shop 4", 15),
    ("Warehouse 2", "Shop 5", 10),
    ("Warehouse 2", "Shop 6", 25),
    ("Warehouse 3", "Shop 7", 20),
    ("Warehouse 3", "Shop 8", 15),
    ("Warehouse 3", "Shop 9", 10),
    ("Warehouse 4", "Shop 10", 20),
    ("Warehouse 4", "Shop 11", 10),
    ("Warehouse 4", "Shop 12", 15),
    ("Warehouse 4", "Shop 13", 5),
    ("Warehouse 4", "Shop 14", 10),
]

# Add all edges to the graph
G.add_weighted_edges_from(edges)

# Positions for drawing the graph
pos = {
    "Terminal 1": (2, 4),
    "Terminal 2": (10, 4),
    "Warehouse 1": (4, 6),
    "Warehouse 2": (8, 6),
    "Warehouse 3": (4, 2),
    "Warehouse 4": (8, 2),
    "Shop 1": (0, 8),
    "Shop 2": (2, 8),
    "Shop 3": (4, 8),
    "Shop 4": (6, 8),
    "Shop 5": (8, 8),
    "Shop 6": (10, 8),
    "Shop 7": (0, 0),
    "Shop 8": (2, 0),
    "Shop 9": (4, 0),
    "Shop 10": (6, 0),
    "Shop 11": (8, 0),
    "Shop 12": (10, 0),
    "Shop 13": (12, 0),
    "Shop 14": (14, 0),
}

# Draw the graph
plt.figure(figsize=(16, 10))
nx.draw(
    G,
    pos,
    with_labels=True,
    node_size=2000,
    node_color="skyblue",
    font_size=10,
    font_weight="bold",
    arrows=True,
)
labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Display the graph
plt.show()
