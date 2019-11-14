visited = [False for i in range(10)]
path = []
def dfs_recursive(graph, start):
    current_vertex = start
    visited[current_vertex]=True
    for neighbor in graph[current_vertex]:
        if visited[neighbor] is False:
            #visited[neighbor] = True
            path.append(neighbor)
            #current_vertex = graph[neighbor][0]
            dfs_recursive(graph, neighbor)

    return path


graph1 = [[1,2], [0,5], [0,3,4], [2], [2,5], [1,4], [7], [6], [9], [8]]
print(dfs_recursive(graph1, 0))
