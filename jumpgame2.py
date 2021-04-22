def jumpgame(self,nums):
    n = len(nums)
    count = 0
    destination = n-1

    curr_coverage,last_jump_index = 0,0

    if n==1:
        return 0

    for i in range(0,n):
        curr_coverage = max(curr_coverage,i+nums[i])

        if i ==last_jump_index:
            last_jump_index = curr_coverage

            count +=1

            if curr_coverage>=destination:
                return count
    return count