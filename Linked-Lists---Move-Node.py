class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest

def move_node(source, dest):
    x=source.data
    source=source.next
    next=dest
    dest=Node(x)
    dest.next=next
    return Context(source, dest)
