

# We have a pipeline, which produces a mapping from every image to a list of up to k near-duplicate images, such as:
# near_dups = {
# "A": ["B", "I", "K"],
# "B": ["A", "D"],
# "C": ["E"],
# "D": [],
# "E": [],
# "F": [],
# "G": ["K"],
# "I": [],
# "K": [],
# }
# Given a mapping such as this one, form clusters: collections of almost identical images.
# In the example above, we would form the following groups: (A, B, D, I, G, K), (C, E), and (F).**

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
# 1. INTEGER n
# 2. INTEGER m
# 3. 2D_INTEGER_ARRAY edges
# 4. INTEGER s
#

from collections import defaultdict

# Function to build the graph
def build_graph(edges, num_of_nodes):
    graph = defaultdict(list)

    # Loop to iterate over every
    # edge of the graph
    for edge in edges:
        a, b = edge[0], edge[1]
        # Creating the graph
        # as adjacency list
        graph[a].append(b)
        graph[b].append(a)
    for n in range(num_of_nodes):
        if n+1 not in graph:
            graph[n+1] = []
    return graph


def BFS_SP(graph, start, goal):
    print("BFS SP started")
    explored = []
    # Queue for traversing the graph in the BFS
    queue = [[start]]
    # Loop to traverse the graph with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1] 
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]
            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # Condition to check if the neighbour node is the goal
                if neighbour == goal:
                    # print("Shortest path = ", new_path)
                    return (len(new_path)-1) * 6
            explored.append(node)
    # Condition when the nodes are not connected
    # print("So sorry, but a connecting path doesn't exist :(")
    return -1


def find_graph_component(graph, start):
    print("BFS SP started")
    explored = []
    # Queue for traversing the graph in the BFS
    queue = [[start]]
    # Loop to traverse the graph with the help of the queue
    while queue:
        path = queue.pop(0)
        node = path[-1] 
        # Condition to check if the
        # current node is not visited
        if node not in explored:
            neighbours = graph[node]
            # Loop to iterate over the
            # neighbours of the node
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                # Condition to check if the neighbour node is the starting one
                # if neighbour == start:
                #     # print("Came to start again")
                #     return explored
            explored.append(node)
    # Condition when the nodes are not connected
    # print("So sorry, but a connecting path doesn't exist :(")
    return explored


def bfs(n, m, edges):
    '''
    n - number of nodes
    m - number of edges
    edges - start and end nodes for edges
    s - start node
    '''
    main_graph = build_graph(edges, n)
    print(f'Main graph is: {main_graph}')
    nodes_to_pass_through = [i+1 for i in range(n)]
    components = []
    while len(nodes_to_pass_through) > 0:
        print("nodes_to_pass_through:", nodes_to_pass_through)
        node_to_pass_through = nodes_to_pass_through[0]
        # nodes_to_pass_through.remove(node_to_pass_through)
        component = find_graph_component(main_graph, node_to_pass_through)
        print(f'Component found: {sorted(component)}')
        for c in component:
            nodes_to_pass_through.remove(c)
        components.append(sorted(component))
    return components


if __name__ == "__main__":
    # Query 1
    num_of_nodes, num_of_edges = 4, 2
    edges = [[1, 2], [1, 3]]

    answer = bfs(num_of_nodes, num_of_edges, edges)
    print(f"Query: components found: {answer}")

    # Query 2
    num_of_nodes, num_of_edges = 3, 1
    edges = [[2, 3]]

    answer = bfs(num_of_nodes, num_of_edges, edges)
    print(f"Query: components found: {answer}")

    # Query 3
    num_of_nodes, num_of_edges = 9, 1
    edges = [[1, 2], [1, 8], [1, 9], [2, 1], [2, 4], [3, 5], [7, 9]]

    answer = bfs(num_of_nodes, num_of_edges, edges)
    print(f"Query: components found: {answer}")
