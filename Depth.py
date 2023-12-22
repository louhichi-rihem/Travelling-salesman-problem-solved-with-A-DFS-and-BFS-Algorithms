# This class represent a graph
class Graph:
    # Initialize the class
    def __init__(self, graph_dict=None, directed=True):
        self.graph_dict = graph_dict or {}
        self.directed = directed
        if not directed:
            self.make_undirected()

    # Create an undirected graph by adding symmetric edges
    def make_undirected(self):
        for a in list(self.graph_dict.keys()):
            for (b, dist) in self.graph_dict[a].items():
                self.graph_dict.setdefault(b, {})[a] = dist

    # Add a link from A and B of given distance, and also add the inverse link if the graph is undirected
    def connect(self, A, B, distance=1):
        self.graph_dict.setdefault(A, {})[B] = distance
        if not self.directed:
            self.graph_dict.setdefault(B, {})[A] = distance

    # Get neighbors or a neighbor
    def get(self, a, b=None):
        links = self.graph_dict.setdefault(a, {})
        if b is None:
            return links
        else:
            return links.get(b)

    # Return a list of nodes in the graph
    def nodes(self):
        s1 = set([k for k in self.graph_dict.keys()])
        s2 = set([k2 for v in self.graph_dict.values() for k2, v2 in v.items()])
        nodes = s1.union(s2)
        return list(nodes)


# This class represent a node
class Node:
    # Initialize the class
    def __init__(self, name: str, parent: str):
        self.name = name
        self.parent = parent
        self.g = 0  # Distance to start node
        self.h = 0  # Distance to goal node
        self.f = 0  # Total cost

    # Compare nodes
    def __eq__(self, other):
        return self.name == other.name

    # Sort nodes
    def __lt__(self, other):
        return self.f < other.f

    # Print node
    def __repr__(self):
        return ('({0},{1})'.format(self.position, self.f))


# Depth-first search (DFS)
def depth_first_search(graph, start, end):
    # Create lists for open nodes and closed nodes
    open = []
    closed = []
    # Create a start node and an goal node
    start_node = Node(start, None)
    goal_node = Node(end, None)
    # Add the start node
    open.append(start_node)

    # Loop until the open list is empty
    while len(open) > 0:
        # Get the last node (LIFO)
        current_node = open.pop(-1)
        # Add the current node to the closed list
        closed.append(current_node)

        # Check if we have reached the goal, return the path
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node.name + ': ' + str(current_node.g))
                current_node = current_node.parent
            path.append(start_node.name + ': ' + str(start_node.g))
            # Return reversed path
            return path[::-1]
        # Get neighbours
        neighbors = graph.get(current_node.name)
        # Loop neighbors
        for key, value in neighbors.items():
            # Create a neighbor node
            neighbor = Node(key, current_node)
            # Check if the neighbor is in the closed list
            if (neighbor in closed):
                continue
            # Check if neighbor is in open list and if it has a lower f value
            if (neighbor in open):
                continue
            # Calculate cost so far
            neighbor.g = current_node.g + graph.get(current_node.name, neighbor.name)
            # Everything is green, add neighbor to open list
            open.append(neighbor)
    # Return None, no path is found
    return None


# The main entry point for this module
def Depth():
    # Create a graph
    graph = Graph()
    # Create graph connections (Actual distance)
    graph.connect('A', 'B', 111)
    graph.connect('A', 'C', 85)
    graph.connect('C', 'D', 104)
    graph.connect('D', 'B', 140)
    graph.connect('D', 'E', 183)
    graph.connect('E', 'F', 200)
    graph.connect('F', 'G', 50)
    graph.connect('D', 'F', 160)
    graph.connect('B', 'G', 160)

    # Make graph undirected, create symmetric connections
    graph.make_undirected()
    # Create heuristics (straight-line distance, air-travel distance)


    # Run search algorithm
    print("Depth Search")
    path = depth_first_search(graph,'A', 'G')
    dis = 0
    for i in path:
        dis = dis + int(i[3:])

    print('Total distance from A to G =', dis)
    print(path)
    print()


if __name__ == "__main__": Depth()


