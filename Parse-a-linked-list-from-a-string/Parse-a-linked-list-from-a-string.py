from preloaded import Node

def linked_list_from_string(list_repr: str) -> Node | None:
    """jvh"""
    if list_repr=='None':
        return None
    lst=list_repr.split(' -> ')[::-1][1:]
    node=Node(int(lst[0]))
    for a in lst[1:]:
        node=Node(int(a), node)
    return node
