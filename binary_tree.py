from collections import deque
class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs(node):
    queue = deque([node])
    output = []
    while queue:
        curr = queue.popleft()
        if curr:
            output.append(curr.val)
            queue.append(curr.left)
            queue.append(curr.right)
    return output

def dfs_iter_preorder(node):
    stack = [node]
    output = []
    while stack:
        curr = stack.pop()
        if curr:
            output.append(curr.val)
            stack.append(curr.right)
            stack.append(curr.left)
    return output

def dfs_recur_inorder(node):
    if not node:
        return []
    return dfs_recur_inorder(node.left) + [node.val] + dfs_recur_inorder(node.right)

def dfs_recur_preorder(node):
    if not node:
        return []
    return [node.val] + dfs_recur_preorder(node.left) + dfs_recur_preorder(node.right)

def dfs_recur_postorder(node):
    if not node:
        return []
    return dfs_recur_postorder(node.left) + dfs_recur_postorder(node.right) + [node.val]

def bfs_level_order(node):
    queue = deque([node])
    output = []
    while queue:
        level = []
        len_queue = len(queue)
        for i in range(len_queue):
            curr = queue.popleft()
            if curr:
                level.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
        if level:
            output.append(level)
    return output

def right_view(node):
    queue = deque([node])
    output = []
    while queue:
        level = []
        len_queue = len(queue)
        for i in range(len_queue):
            curr = queue.popleft()
            if curr:
                level.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
        if level:
            output.append(level[-1])
    return output

def left_view(node):
    queue = deque([node])
    output = []
    while queue:
        level = []
        len_queue = len(queue)
        for i in range(len_queue):
            curr = queue.popleft()
            if curr:
                level.append(curr.val)
                queue.append(curr.left)
                queue.append(curr.right)
        if level:
            output.append(level[0])
    return output

'''
        1
      /   \
    2       3
  /   \
4       5
'''
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print('BFS: ', bfs(root))
print('DFS iter preorder: ', dfs_iter_preorder(root))
print('DFS recur inorder: ', dfs_recur_inorder(root))
print('DFS recur preorder: ', dfs_recur_preorder(root))
print('DFS recur postorder: ', dfs_recur_postorder(root))
print('BFS levelorder: ', bfs_level_order(root))
print('right view: ', right_view(root))
print('left view: ', left_view(root))
