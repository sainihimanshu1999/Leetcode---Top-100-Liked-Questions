def solve(self,nums):
    sorted_nums = sort(nums)
    end = len(nums)-1
    start = 0

    if sorted_nums == nums:
        return 0

    while sorted_nums[start] == nums[start]:
        start += 1

    while sorted_nums[end] == nums[end]:
        end -=1

    return end+1-start