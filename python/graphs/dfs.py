from graphs import Graph

def dfs_visit(graph, source, parent, finished):
    for u in graph.adj_list(source):
        if u not in parent:
            parent[u] = source
            dfs_visit(graph, u, parent, finished)
    finished.append(source)

def dfs(graph):
    parent = {}
    finished = []
    vertices = graph.vertices()
    for v in vertices:
        if v not in parent:
            parent[v] = None
            dfs_visit(graph, v, parent, finished)
    finished = list(reversed(finished))
    return parent, finished
    
if __name__ == '__main__':
    g = Graph()
    for key in [1, 2, 3, 4]:
        g.add_node(key)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 1)
    print(dfs(g))
