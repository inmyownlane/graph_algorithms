# An undirected graph is Eulerian if: 1) The graph is connected, and 2) All vertices have an even degree.

def is_eulerian(graph):

    '''
    Checks if an undirected graph is Eulerian.
    :param graph: A dictionary representing the adjacency list of a graph.
    :return: True if the graph is Eulerian, False otherwise
    '''

    def is_connected(graph):

        # initialising a starting node.
        start_node = None

        # iterates through each node, looking for a node that has edges
        for node, neighbors in graph.items():
            if neighbors:
                start_node = node
                break
            # if there's no nodes with edges, it is trivially Eulerian. 
            if start_node is None:
                return True

        # Perform DFS to check for connectivity, satisfying the 1st criteria for whether a graph is Eulerian or not
        visited = set()

        def dfs(node):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(start_node)

        for node, neighbors in graph.items():
            if neighbors and node not in visited:
                return False
        return True
    
    # Criteria 1) Check for connectivity of the graph
    if not is_connected(graph):
        return False
    
    # Criteria 2) Check if every vertex has even degree
    for node in graph:
        if len(graph[node]) % 2 != 0:
            return False
    
    # Return True if both criterias are met
    return True

# Example
graph1 = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1]
}

print(is_eulerian(graph1))