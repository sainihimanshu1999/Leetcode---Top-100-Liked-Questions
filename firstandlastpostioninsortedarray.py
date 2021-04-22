def solve(nums, target):
    if not nums:
        return [-1,-1]

    if target not in nums:
        return [-1,-1]

    a = []
    n = len(nums)-1

    for i in nums:
        if i == target:
            a.append(nums.index(i))
            break
    
    num.sort(reverse = True)
    for i in nums:
        if i == target:
            n.append(n-(nums.index(i)))
            break

    return a
