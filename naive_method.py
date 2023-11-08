import networkx as nx
from itertools import combinations

# Improved function to count only connected graphlets of a given size in a graph
def count_connected_graphlets(G, size):
    # Dictionary to hold graphlet counts
    graphlet_counts = {}
    
    # Iterate over all combinations of nodes of the given size
    for nodes in combinations(G.nodes(), size):
        # Induce subgraph from each combination of nodes
        subgraph = G.subgraph(nodes)
        # Check if the subgraph is connected
        if nx.is_connected(subgraph):
            # Get the degree sequence of the subgraph (sorted)
            degree_sequence = tuple(sorted([subgraph.degree(n) for n in nodes]))
            # Increment count in dictionary
            graphlet_counts[degree_sequence] = graphlet_counts.get(degree_sequence, 0) + 1
    
    return graphlet_counts

# Count connected graphlets of size 3 (triangles and two-star chains)
connected_graphlet_counts = count_connected_graphlets(G, 3)

# Output the counts of the connected graphlets
print(connected_graphlet_counts)
