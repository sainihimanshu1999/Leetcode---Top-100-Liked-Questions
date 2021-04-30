def reverse(self,head):
    if not head:
        return None

    prev = None
    curr = head
    while curr:
        new = curr.next
        curr.next = prev
        prev = curr
        curr = new
    prev = head
    return head