class Graph:

    def __init__(self):
        self.vertex_collection = []
        
    def __str__(self):
        return self.vertex_collection


    def add_node(self, value):
        vertex = Vertex(value)
        if vertex not in self.vertex_collection:
            self.vertex_collection.append(vertex)
        return vertex


    def add_edge(self, vertex1, vertex2, weight=1):
        if vertex1 in self.vertex_collection and vertex2 in self.vertex_collection:
                edge = Edge(vertex2, weight)
                vertex1.adjacency_list.append([vertex2, edge])
        else:
            raise KeyError
        

    def get_nodes(self):
        if len(self.vertex_collection) >= 1:
            return self.vertex_collection
        return None


    def get_neighbors(self, vertex):
        idx = self.vertex_collection.index(vertex)
        neighbors = []
        for neighbor in self.vertex_collection[idx].adjacency_list:
            neighbors.append(neighbor[1])
        return neighbors

    def size(self):
        return len(self.vertex_collection)


    def depth_first_search(self, vertex):
        stack =[]
        collection = []
        visited = set()
        if len(self.vertex_collection) <= 0: return []
        stack.append(vertex)
        visited.add(vertex.value)
        while len(stack):
            node = stack.pop()
            collection.append(node.value)
            for i in reversed(range(len(node.adjacency_list))):
                if node.adjacency_list[i][0].value not in visited:
                    stack.append(node.adjacency_list[i][0])
                visited.add(node.adjacency_list[i][0].value)
        return collection

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacency_list = []

    def __str__():
        return


class Edge:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight


if __name__ == "__main__":
    g = Graph()
    apple = g.add_node("apple")
    banana = g.add_node("banana")
    g.add_edge(apple, banana, 5)
    neighbors = g.get_neighbors(apple)
    print(neighbors[0])
    print(g.depth_first_search(apple))