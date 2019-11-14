def topo_sort(graph):
    in_degrees = [0 for i in range(len(graph))]

    visited, queue = [], []
    #get the in degrees
    for parent in graph:
        if parent:
            for child in parent:
                in_degrees[child]+=1
        #in_degrees[vertex] = len(graph[vertex])
    print(in_degrees)

    #in_degrees_mod = in_degrees
    for i in range(len(in_degrees)):
        if in_degrees[i]==0:
            queue.append(i)
    print(queue)
    #exit()
    while queue:
        current_vertex = queue.pop(0)
        visited.append(current_vertex)
        for child in graph[current_vertex]:
            in_degrees[child] -=1
            if in_degrees[child]==0:
                queue.append(child)
    return visited

graph1 =[[], [], [3],[1],[0,1], [2,0]]
         #[[5,4], [3,4], [5], [2], [], []]
print(topo_sort(graph1))

