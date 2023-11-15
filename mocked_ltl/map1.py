import json


class Graph:
    def __init__(self, size):
        self.adj_matrix = [["" for _ in range(size)] for _ in range(size)]

    def add_edge(self, u, v, val=""):
        self.adj_matrix[v][u] = val

    def print_matrix(self):
        for row in self.adj_matrix:
            print(row)

    def to_serializable(self):
        return self.adj_matrix


# Example usage
size = 6
g = Graph(size)
prompt = "F & h F & c F & d F & b F a"
g.add_edge(0, 1, "a")
g.add_edge(0, 2, "a & b")
g.add_edge(0, 3, "a & b & d")
g.add_edge(0, 4, "a & b & c & d")
g.add_edge(0, 5, "a & b & c & d & h")

g.add_edge(1, 2, "!a & b")
g.add_edge(1, 3, "!a & b & d")
g.add_edge(1, 4, "!a & b & c & d")
g.add_edge(1, 5, "!a & b & c & d & h")

g.add_edge(2, 3, "!b & d")
g.add_edge(2, 4, "!b & c & d")
g.add_edge(2, 5, "!b & c & d & h")

g.add_edge(3, 4, "c & !d")
g.add_edge(3, 5, "c & !d & h")

g.add_edge(4, 5, "!c & h")

g.print_matrix()

serializable_graph = g.to_serializable()

# Save to JSON file
with open("map1.json", "w") as json_file:
    json.dump(serializable_graph, json_file, indent=4)
