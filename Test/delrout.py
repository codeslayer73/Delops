class Dijkstra:

    def __init__(self, vertices, graph):
        self.vertices = vertices  # ("A", "B", "C" ...)
        self.graph = graph  # {"A": {"B": 1}, "B": {"A": 3, "C": 5} ...}

    def find_route(self, start, end):
        unvisited = {n: float("inf") for n in self.vertices}
        unvisited[start] = 0  # set start vertex to 0
        visited = {}  # list of all visited nodes
        parents = {}  # predecessors
        while unvisited:
            # get smallest distance
            min_vertex = min(unvisited, key=unvisited.get)
            for neighbour, _ in self.graph.get(min_vertex, {}).items():
                if neighbour in visited:
                    continue
                new_distance = unvisited[min_vertex] + \
                    self.graph[min_vertex].get(neighbour, float("inf"))
                if new_distance < unvisited[neighbour]:
                    unvisited[neighbour] = new_distance
                    parents[neighbour] = min_vertex
            visited[min_vertex] = unvisited[min_vertex]
            unvisited.pop(min_vertex)
            if min_vertex == end:
                break
        return parents, visited

    @staticmethod
    def generate_path(parents, start, end):
        path = [end]
        while True:
            key = parents[path[0]]
            path.insert(0, key)
            if key == start:
                break
        return path


input_vertices = ("A", "B", "D", "E")
input_graph = {
    "A": {"B": 30, "D": 60, "E": 45},
    "B": {"A": 30, "D": 40},
    "D": {"A": 60, "B": 40, "E": 20},
    "E": {"A": 45, "D": 20}
}
start_vertex = "A"
end_vertex = "D"
dijkstra = Dijkstra(input_vertices, input_graph)
p, v = dijkstra.find_route(start_vertex, end_vertex)
print("Distance from %s to %s is: %.2f Km" %
      (start_vertex, end_vertex, v[end_vertex]))
se = dijkstra.generate_path(p, start_vertex, end_vertex)
print("Path from %s to %s is: %s " %
      (start_vertex, end_vertex, " -> ".join(se)))
