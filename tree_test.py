class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs(root, low, high):
    # bfs
    range_sum = 0
    queue = [root]        
    while queue:
        curr = queue.pop(0)
        if curr:
            if low <= curr.val <= high:
                range_sum += curr.val
            if low < curr.val:
                queue.append(curr.left)
            if curr.val < high:
                queue.append(curr.right)                
    return range_sum

def dfs(root, low, high):
    # dfs
    range_sum = 0
    stack = [root]
    while stack:
        curr = stack.pop()
        if curr:
            if low <= curr.val <= high:
                range_sum += curr.val
            if low < curr.val:
                    stack.append(curr.left)
            if curr.val < high:
                    stack.append(curr.right)
    return range_sum

tree = TreeNode(10)
tree.left = TreeNode(5)
tree.left.left = TreeNode(3)
tree.left.right = TreeNode(7)
tree.right = TreeNode(15)
tree.right.right = TreeNode(18)

_sum = bfs(tree, 7,15)
print(_sum)
_sum = dfs(tree, 7,15)
print(_sum)