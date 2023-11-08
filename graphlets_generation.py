import matplotlib.pyplot as plt
import networkx as nx
def generate_graphlet(input):             #input: a graph
    graphs = []
    new_graphs = [g for g in nx.graph_atlas_g() if len(g.nodes())==input]

    for graph in new_graphs:
        if len(list(nx.connected_components(graph))) == 1:      #reject the graph with is not connected (would not be the graphlet)
            graphs.append(graph)
    return graphs
graphs = generate_graphlet(5)
nx.draw(graphs[9], with_labels=True, node_size=500, node_color='lightblue', font_size=10, font_color='black')
plt.title("Sample Graph")
plt.show()
print(graphs)