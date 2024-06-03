from collections import deque
def level_order(root):
    queue = deque([root])
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

class Node():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

root = Node(3)
root.left = Node(9)
root.right = Node(20)
root.right.left = Node(15)
root.right.right = Node(7)
print(level_order(root))