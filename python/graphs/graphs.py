class Graph:
    #TODO make this graph able to be directed
    def __init__(self):
        self.adjacency_lists = {}

    def vertices(self):
        return self.adjacency_lists.keys()

    def add_node(self, key):
        if key in self.adjacency_lists:
            raise Error("add_node: key is already in the graph")
        else:
            self.adjacency_lists[key] = []

    #TODO check for adding duplicate edges
    def add_edge(self, u, v):
        if not (u in self.adjacency_lists and v in self.adjacency_lists):
            raise Error("add_edge: node is not in the graph")
        else:
            self.adjacency_lists[u].append(v)
            self.adjacency_lists[v].append(u)

    def adj_list(self, node):
        return self.adjacency_lists[node]

    def __contains__(self, node):
        return node in self.adjacency_lists

    def __str__(self):
        return str(self.adjacency_lists)

if __name__ == '__main__':
    # create a square graph
    g = Graph()
    for key in [1, 2, 3, 4]:
        g.add_node(key)
    g.add_edge(1, 2)
    g.add_edge(2, 3)
    g.add_edge(3, 4)
    g.add_edge(4, 1)
    g.add_edge(1, 3)
    print(g)
    print(1 in g)
