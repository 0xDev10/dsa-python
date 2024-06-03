# def dfs(graph, node, visited=set()):
#     if node not in visited:
#         visited.add(node)
#         for child in graph[node]:
#             dfs(graph, child, visited)
#         return visited

def dfs(graph, node):
    visited = []
    stack = [node]    

    while stack:        
        curr = stack.pop()
        if curr not in visited:
            visited.append(curr)
            if curr in graph:
                for child in graph[curr]:
                    stack.append(child)
    return visited

# gdict = { 
#    "a" : set(["b","c"]),
#    # "b" : set(["a", "d"]),
#    "c" : set(["a", "d"]),
#    "d" : set(["e"]),
#    "e" : set(["a"])
# }

gdict = {
  0: [8, 1, 5],
  1: [0],
  5: [0, 8],
  8: [0, 5],
  2: [3, 4],
  3: [2, 4],
  4: [3, 2]
}

sol = dfs(gdict, 0)
print(sol) #['a', 'b', 'd', 'e', 'c']