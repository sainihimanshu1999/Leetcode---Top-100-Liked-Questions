'''
Linked list is sorted using merge sort algorithm
'''

def sortList(self,head):
    if not head or not head.next:
        return head

    fast,slow = head.next,head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    second = slow.next
    slow.next = None

    l = self.sortList(head)
    r = self.sortList(second)

    return self.merge(l,r)

def merge(self,l,r):
    if not l or not r:
        return r or l

    temp = ListNode(0)
    head = temp
    while l and r:
        if l.val<=r.val:
            head.next = l
            l = l.next
        else:
            head.next = r
            r = r.next
        head = head.next
    return temp.next    