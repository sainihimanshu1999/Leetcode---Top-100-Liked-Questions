'''
using an extra space
'''
def palindrome(self,head):
    a = []
    while head:
        a.append(head.val)
        head = head.next

    return a == a[::-1]


'''
reversing the second half and checking
'''
def palindrome(self,head):
    #getting to the middle point
    slow=fast=head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    prev = None
    #reversing the half
    while slow:
        new = slow.next
        slow.next = prev
        prev = slow
        slow = new
    #checking whether reversed and non reversed are equal
    while prev:
        if prev.val != head.val:
            return False
        prev = prev.next
        head = head.next
    return True