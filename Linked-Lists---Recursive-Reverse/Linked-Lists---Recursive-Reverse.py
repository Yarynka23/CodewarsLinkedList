class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if not head:
        return None
    if head.next:
        rev = reverse(head.next)
        head.next.next = head
        head.next = None
        return rev
    else:
        return head
