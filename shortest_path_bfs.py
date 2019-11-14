def bfs(graph, vertex_a, vertex_b):
    visited, que = [], [vertex_a]
    while(len(que)):
        current_vertex = que.pop(0)
        #if current_vertex == vertex_b:
        #    return visited
        if current_vertex not in visited:
            visited.append(current_vertex)
            que.extend(graph[current_vertex])
    return visited


graph1 = [[1,2], [0,5], [0,3,4], [2], [2,5], [1,4], [7], [6], [9], [8]]
print(bfs(graph1, 0, 5))
print(bfs(graph1, 0,3))