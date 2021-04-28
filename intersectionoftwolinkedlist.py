'''
using dictionary
'''
def intersection(self,headA,headB):
    dic = {}
    curr1 = headA
    curr2 = headB

    while curr1:
        dic[curr1] = curr1.val
        curr1 = curr1.next

    while curr2:
        if curr2 in dic:
            return curr2:
        dic[curr2] = curr2.val
        curr2 = curr2.next


'''
using two pointer approach
'''

def intersection(self,headA,headB):
    if not headA or not headB:
        return None

    pA = headA
    pB = headB

    while pA!=pB:
        pA = pA.next if pA else headB
        pB = pB.next if pB else headA
    
    return pA

    