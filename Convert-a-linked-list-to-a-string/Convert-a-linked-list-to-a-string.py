def stringify(node):
    """jvh"""
    if not node:
        return 'None'
    st=str(node.data)+' -> '
    while node.next:
        node=node.next
        st+=str(node.data)+' -> '
    return st+'None'
