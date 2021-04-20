'''
it is done using the priority queue, in python 3 it is done usinf heapq
'''
from Queue import PriorityQueue
def mergeKsortedList(self,lists):
    temp = ListNode(None)
    curr = temp

    q = PriorityQueue()
    for node in lists:
        if node:
            q.put((node.val,node))
    
    while q.size()>0:
        curr.next = q.get()[1]
        curr = curr.next
        if curr.next:
            q.put((curr.next.val, curr.next))

    return curr.next
