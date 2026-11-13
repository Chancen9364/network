import networkx as nx

G = nx.cycle_graph(5)

centrality = nx.eigenvector_centrality_numpy(G)

print(centrality)

#{0: 0.44721359549995776, 1: 0.44721359549995776, 2: 0.44721359549995787, 3: 0.447213595499958, 4: 0.44721359549995787}
