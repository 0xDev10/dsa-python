class Node():
    def __init__(self, val):
        self.val = val
        self.next = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

def traverse_iter(head):
    curr = head
    while curr:
        print(curr.val)
        curr = curr.next

def traverse_recur(head):
    if head:
        print(head.val)
        traverse_recur(head.next)

def reverse_ll(head):
    prev = None
    curr = head
    while curr.next:
        next_node = curr.next
        prev = curr
        curr = curr.next
        curr.next = prev
    return prev


traverse_iter(a)
print('-'*10)
print(reverse_ll(a))
traverse_recur(a)