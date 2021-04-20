def threesum(self,nums):
    nums.sort()
    N,result = len(nums),[]

    #used to remove duplicates in 3 sum
    for i in range(N):
        if i>0 and nums[i] == nums[i-1]:
            continue

        start,end = i , N-1
        target = nums[i]*-1

        while start<end:
            if nums[start]+nums[end] == target:
                result.append([nums[start],nums[end],nums[i]])
                start += 1

                #used to remove duplicates in 2sum
                while start<end and nums[start] == nums[start-1]:
                    start+=1
            elif nums[start]+nums[end]<target:
                start+=1
            else:
                end -=1