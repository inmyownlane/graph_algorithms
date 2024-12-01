def is_connected(graph):

    if not graph:
        return True

    start_node = next(iter(graph))

    visited = set()

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start_node)

    return len(visited) == len(graph)




# Examples:
# graph1 is connected
graph1 = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}

# graph2 is disconnected
graph2 = {
    0: [1],
    1: [0],
    2: []
}

print(f"Is graph1 connected?: ", is_connected(graph1))
print(f"Is graph2 connected?: ", is_connected(graph2))