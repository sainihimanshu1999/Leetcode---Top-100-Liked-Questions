'''
adding two numbers in linked list
'''
def addingtwonumbers(self,A,B):
    var = curr = ListNode(0)
    carry = 0
    while A or B or carry:
        if A:
            carry += A.val
            A = A.next

        if B:
            carry += B.val
            B = B.next

        var.next = ListNode(carry%10)
        var = var.next
        carry //=10
    return curr.next