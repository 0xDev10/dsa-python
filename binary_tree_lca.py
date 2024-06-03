class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lca(node, p, q):
    print('='*10)
    print('lca')
    if not node or node==p or node==q:
        return node
    left = lca(node.left, p, q)
    print('left = ', left)
    right = lca(node.right, p, q)
    print('right = ', right)
    
    if left and right:
        return node
    
    # return left if left else right
    if left:
        print(left.val)
        return left
    else:
        print(right)
        print('-'*10)
        return right

"""
        3
      /   \
    5       1
  /       /   \
2       8       4
lca(3, 5, 2)
left = lca(5, 5, 2) = 5
right = lca(1, 5, 2) = None
"""

tree = Node(3)
tree.left = Node(5)
tree.left.left = Node(2)
tree.right = Node(1)
tree.right.left = Node(8)
tree.right.right = Node(4)
p = tree.left.left
q = tree.left
lca_node = lca(tree, p, q)
print(lca_node.val)