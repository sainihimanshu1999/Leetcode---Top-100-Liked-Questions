'''
using dictionary
'''
def cycle(self,head):
    dic = {}
    curr = head

    while curr:
        if curr in dic:
            return True
        else:
            dic[curr] = curr.val
    return False

'''
Using two pointer approach
'''

def cycle(self,head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False