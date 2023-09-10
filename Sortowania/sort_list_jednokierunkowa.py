class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def sort(p, q):
    head = Node()
    n = head
    while p is not None and q is not None:
        if p.next.val < q.next.val:
            n.next = p.next
            p.next = p.next.next
        else:
            n.next = q.next
            q.next = q.next.next
        n = n.next
    if p.next != None:
        n.next = p.next
    else:
        n.next = q.next

