'''
Here the time complexity is O(n^2), but on the other hand it is the easisest solution
'''

def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area = 0
        n = len(height)
        for i in range(n):
            for j in range(i+1,n):
                area = max(area,min(height[j],height[i])*(j-i))
        return area


'''
here the time complexity is O(n), here we are intialising two index, firstpointer at start
lastpointer at last, and then comparing these two, if fp<lp, then we increase fp and if lp<fp,
we decrease lp, as fp and lp are only indexes
'''

def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        fp = 0
        lp = len(height)-1
        area = 0
        
        while fp<lp:
            area = max(area,min(height[fp],height[lp])*(lp-fp))
            
            if height[fp]<height[lp]:
                fp += 1
            else:
                lp -=1
        return area
                
        