def is_route(graph, vertex_a, vertex_b):

    #start dfs traversal from vertex_a and see if we can reach b (or wheter b is in the visited)
    visited, stack = [], [vertex_a]
    while(len(stack)):
        current_vertex = stack.pop()
        if current_vertex == vertex_b:
            return True
        if current_vertex not in visited:
            visited.append(current_vertex)
            stack.extend(graph[current_vertex])

    return False

graph1 = [[1,2], [0,5], [0,3,4], [2], [2,5], [1,4], [7], [6], [9], [8]]
print(is_route(graph1, 0, 5))
print(is_route(graph1, 0, 6))