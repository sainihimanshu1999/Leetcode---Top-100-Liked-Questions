class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(self, l1, l2):
        var = curr = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2  = l2.next
            
            curr.next = ListNode(carry%10)
            curr = curr.next
            carry //=10
        return var.next
        
'''
adding two linked list, it is the most time efficient technique. one more method can be used
traversing both the strings and adding there values, if carry get more than 10, do the floor of it and
if either of the list ends imagine zero for all other values of it
'''