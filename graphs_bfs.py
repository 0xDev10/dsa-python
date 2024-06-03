def bfs(graph, node):
    visited = [node]
    queue = [node]

    while queue:
        curr = queue.pop(0)
        if curr in graph:
            for child in graph[curr]:
                if child not in visited:
                    visited.append(child)
                    queue.append(child)

    return visited

# def bfs(graph, node):
#     visited = []
#     stack = [node]    

#     while stack:        
#         curr = stack.pop()
#         if curr not in visited:
#             visited.append(curr)
#             if curr in graph:
#                 for child in graph[curr]:
#                     stack.append(child)
#     return visited

gdict = { 
    "a" : set(["b","c"]),
    # "b" : set(["a", "d"]),
    "c" : set(["a", "d"]),
    "d" : set(["e"]),
    "e" : set(["a"])
}

sol = bfs(gdict, "a")
print(sol)