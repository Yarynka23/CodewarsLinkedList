from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next

def get_nth(node, index):
    if not isinstance(node, Node):
        raise ValueError
    if index<0:
        raise ValueError
    final=node
    for a in range(index):
        if not final.next:
            raise ValueError
        final=final.next
    return final
