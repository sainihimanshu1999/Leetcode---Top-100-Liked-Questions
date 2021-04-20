def removenthnodefromthelist(self,head,n):
    slow = fast = head
    for i in range(n):
        fast = fast.next

    if not fast.next:
        return head.next

    while fast.next:
        slow = slow.next
        fast = fast.next

    slow.next = slow.next.next
    return head