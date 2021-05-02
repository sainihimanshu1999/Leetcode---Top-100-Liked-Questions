from collections import deque
def slidingmaximum(self,nums,k):
    if not nums:
        return []

    if k == 0:
        return 0

    q = deque()
    result = []

    for i in range(k):
        while len(q)!=0:
            if nums[i]>nums[q[-1]]:
                q.pop()
            else:
                break
        q.append(i)

    for i in range(k,len(nums)):
        result.append(nums[q[0]])

        if q[0]<i-k+1:
            q.popleft()

        while len(q)!=0:
            if nums[i]>nums[q[-1]]:
                q.pop()
            else:
                break
        q.append(i)

    result.append(nums[q[0]])
    return result

