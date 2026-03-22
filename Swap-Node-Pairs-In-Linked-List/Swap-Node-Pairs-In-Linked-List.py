from preloaded import Node

def swap_pairs(head):
    n = Node()
    n.next = head
    next = n
    while next.next and next.next.next:
        a = next.next
        b = next.next.next
        a.next = b.next
        b.next = a
        next.next = b
        next = a
    return n.next
