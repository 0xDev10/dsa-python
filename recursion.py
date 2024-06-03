
# def recursion(n):
#     print(n)
#     if n == 0:
#         return 0
#     else:
#         return recursion(n-1)

# n = 4
# recur = recursion(n)
# print(recur)

def recursion(n, l):
    if n == 0:
        return l.append(n)
    else:
        l.append(n-1)
        return recursion(n-1, l)

n = 4
l = []
recur = recursion(n, l)
print(recur)
    