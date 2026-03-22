class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates(head):
    next=head
    while next and next.next:
        if next.data==next.next.data:
            next.next=next.next.next
        else:
            next=next.next
    return head
