def loop_size(node):
    fast=node
    slow=node
    while fast and fast.next:
        fast=fast.next.next
        slow=slow.next
        if slow==fast:
            break
    counter=0
    while True:
        fast=fast.next.next
        slow=slow.next
        counter+=1
        if slow==fast:
            break
    return counter
