def jumpgame(sele,nums):
    destination,curr_coverage,last_jump_index,jumps = len(nums)-1,0,0,0
    if len(nums)==1:
        return True

    for i in range(len(nums)):
        curr_coverage = max(curr_coverage,i+nums[i])

        if i == last_jump_index:
            last_jump_index = curr_coverage
            jumps+=1

            if curr_coverage>=destination:
                return True
    return False
