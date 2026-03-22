class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if not head or not head.next:
        raise ValueError
    next=head
    f=[]
    s=[]
    first=None
    second=None
    while next:
        if next.next:
            f.append(next.data)
            s.append(next.next.data)
            next=next.next.next
        else:
            f.append(next.data)
            break
    for a in f[::-1]:
        n=first
        first=Node(a)
        first.next=n
    for a in s[::-1]:
        n=second
        second=Node(a)
        second.next=n
    return Context(first, second)
