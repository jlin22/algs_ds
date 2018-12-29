from graphs import Graph

def bfs(graph, source):
    if source not in graph.vertices():
        raise Error("bfs: source is not in graph")
    parent = {source: None}
    levels = {source: 0}
    current_level = 1
    frontier = [source]
    
    while frontier:
        next_frontier = []
        for u in frontier:
            for v in graph.adj_list(u):
                if v not in parent:
                    parent[v] = u
                    levels[v] = current_level
                    next_frontier.append(v)
        current_level += 1
        frontier = next_frontier
    return (parent, levels)

if __name__ == '__main__':
    g = Graph()
    for key in [1, 2, 3, 4]:
        g.add_node(key)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 1)
    print(g)
    parent, levels = bfs(g, 1)
    print(parent, levels)
