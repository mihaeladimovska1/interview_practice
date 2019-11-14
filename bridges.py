def get_bridges(graph, start_vertex):
    visited = [False for i in range(len(graph))]
    height_stacked = [0 for i in range(len(graph))] #low
    height_visited = [0 for i in range(len(graph))] #disc
    stack = [start_vertex]
    bridges = []
    parents = []
    previous_vertex = start_vertex
    stack_level = 0
    visited_level = 0
    while stack:
        current_vertex = stack.pop()
        print(current_vertex)

        if not visited[current_vertex]:
            visited[current_vertex] = True

            height_visited[current_vertex] = visited_level
            visited_level += 1

            stack.extend(graph[current_vertex])
            stack_level+=1


            for neighbor in graph[current_vertex]:
                if not visited[neighbor]:
                    height_stacked[neighbor]=stack_level

            if height_visited[current_vertex] > height_stacked[previous_vertex]:
                bridges.append([current_vertex, previous_vertex])
            previous_vertex = current_vertex

    return bridges

graph1 = [[1,2], [0,2], [0,1,3,4], [2,4],[2,3,5], [4,6],[5]]
print(get_bridges(graph1,0))