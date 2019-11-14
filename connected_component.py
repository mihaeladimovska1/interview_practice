import numpy as np

#dfs traversal, assuming we have the graph is given as adj. list
def dfs(graph, start_vertex):
    visited, stack = [], [start_vertex]
    while len(stack):
        current_vertex = stack.pop()
        if current_vertex not in visited:
            visited.append(current_vertex)
            stack.extend(graph[current_vertex])
    return visited

def get_connected_comp(graph):
    components = []
    traversed_vertices = []
    comp = dfs(graph, 0)
    components.append(comp)
    for i in comp:
        traversed_vertices.append(i)
    print(len(traversed_vertices), "here")
    #for j in range(2):
    while len(traversed_vertices)!=len(graph):
        start_vertex = np.setdiff1d([i for i in range(len(graph))], traversed_vertices)[0]#[i for i in [x for x in range(len(graph))] not in comp][0]
        print(start_vertex, "here2")
        comp = dfs(graph, start_vertex)
        print(comp, "here3")

        for i in comp:
            traversed_vertices.append(i)
        print(traversed_vertices, "here4")
        print(len(traversed_vertices))
        #exit()
        components.append(comp)
    return components

def dfs2(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex])
    return visited

graph1 = [[1,2], [0,5], [0,3,4], [2], [2,5], [1,4], [7], [6], [9], [8]]
print(dfs(graph1, 0))
print(dfs2(graph1, 0))
print(get_connected_comp(graph1))