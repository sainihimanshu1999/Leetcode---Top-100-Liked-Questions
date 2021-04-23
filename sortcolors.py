'''
Red is represented by 0, white is represented by 1, blue is represented by 2
'''

def sortColors(self,nums):
    red,white,blue = 0,0,len(nums)-1

    while white<=blue:
        if nums[white] == 0:
            nums[red],nums[white] = nums[white],nums[red]
            red+=1
            white+=1
        elif nums[white] == 1:
            white += 1
        else:
            nums[white],nums[blue] = nums[blue],nums[white]
            blue -=1


'''
Since they are represented by a number, and all the colrs need to be together the can be
sorted as we sort normally
'''
def sortColors(self,nums):
    nums.sort()
