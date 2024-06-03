class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_bst(nodes):
    if nodes == []:
        return None
    mid = len(nodes)//2
    node = Node(nodes[mid])
    node.left = insert_bst(nodes[:mid])
    node.right = insert_bst(nodes[mid+1:])
    return node

nodes = [1,2,3,4]
print(insert_bst(nodes))