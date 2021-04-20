'''
Using Dummy variable
'''
def mergetwolists(self,l1,l2):
    curr = temp = ListNode(0)

    while l1 and l2:
        if l1.val<l2.val:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next

        temp = temp.next
    temp.next = l1 or l2
    return curr.next


'''
using recurrsion
'''

def mergeList(self,l1,l2):
    if not l1 or not l2:
        return l1 or l2

    if l1.val<l2.val:
        l1.next = self.mergeList(l1.next,l2)
        return l1

    else:
        l2.next = self.mergeList(l2,l2.next)
        return l2

    
