class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bfs(root):
    # bfs
    nodes = []
    queue = [root]        
    while queue:
        curr = queue.pop(0)
        if curr:
            nodes.append(curr.val)
            queue.append(curr.left)
            queue.append(curr.right)
    return nodes

def dfs(root, traversal='inorder'):
    # dfs
    if traversal=='inorder':
        nodes = []
        stack = []
        curr = root
        while stack or curr:
            if curr:
                stack.append(curr)
                curr = curr.left
            else:
                curr = stack.pop()
                nodes.append(curr.val)
                curr = curr.right
        return nodes

tree = TreeNode('A')
tree.left = TreeNode('B')
tree.left.left = TreeNode('D')
tree.left.right = TreeNode('E')
tree.right = TreeNode('C')
tree.right.left = TreeNode('F')
tree.right.right = TreeNode('G')

"""
        A
    B       C
D      EF       G
"""

_sum = bfs(tree)
print('BFS')
print(_sum)
print('\nDFS inorder')
_sum = dfs(tree)
print(_sum)