# Routing algorithm done based on the logic of Eulerean circuit
def route(adj):

    # adj represents the adjacency list of
    # the directed graph
    # edge_count represents the number of edges
    # emerging from a vertex
    edge_count = dict()

    for i in range(len(adj)):

        # find the count of edges to keep track
        # of unused edges
        edge_count[i] = len(adj[i])

    if len(adj) == 0:
        return  # empty graph

    # Maintain a stack to keep vertices
    curr_path = []

    # vector to store final circuit
    circuit = []

    # start from any vertex
    curr_path.append(0)
    curr_v = 0  # Current vertex

    while len(curr_path):

        # If there's remaining edge
        if edge_count[curr_v]:

            # Push the vertex
            curr_path.append(curr_v)

            # Find the next vertex using an edge
            next_v = adj[curr_v][-1]

            # and remove that edge
            edge_count[curr_v] -= 1
            adj[curr_v].pop()

            # Move to next vertex
            curr_v = next_v

        # back-track to find remaining circuit
        else:
            circuit.append(curr_v)

            # Back-tracking
            curr_v = curr_path[-1]
            curr_path.pop()

    # we've got the circuit, now print it in reverse
    for i in range(len(circuit) - 1, -1, -1):
        print(circuit[i], end="")
        if i:
            print(" -> ", end="")


if __name__ == "__main__":

    # Input Graph 1
    demand_route1 = [0] * 3
    for i in range(3):
        demand_route1[i] = []

    # Build the edges
    print("Test Case 1")
    print("\nBased on the order array which is filtered to a recommended set of orders all are appended:")
    demand_route1[0].append(1)
    demand_route1[1].append(2)
    demand_route1[2].append(0)
    route(demand_route1)
    print("\nSuggested cyclic path: ")
    print()

    # Input Graph 2
    demand_route2 = [0] * 7
    for i in range(7):
        demand_route2[i] = []
    print("Test Case 2")
    print("\nBased on the order array which is filtered to a recommended set of orders all are appended:")
    demand_route2[0].append(1)
    demand_route2[0].append(6)
    demand_route2[1].append(2)
    demand_route2[2].append(0)
    demand_route2[2].append(3)
    demand_route2[3].append(4)
    demand_route2[4].append(2)
    demand_route2[4].append(5)
    demand_route2[5].append(0)
    demand_route2[6].append(4)
    print("\nSuggested cyclic path: ")
    route(demand_route2)
    print()
