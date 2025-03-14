from graph import create_graph, get_degree, dfs_traversal, bfs_traversal, find_shortest_path, visualize_graph

def run_test():
    edges = [(1,2), (2,3), (3,4)]
    G = create_graph(edges)

    node = 2
    get_degree(G, node)

    start = 1
    dfs_traversal(G, start)

    start = 2
    bfs_traversal(G, start)

    source, target = 2,4
    find_shortest_path(G, source, target)

    visualize_graph(G)

run_test()
