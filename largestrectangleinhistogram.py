def maxArea(self,heights):
    stack = [-1]
    heights.append(0)
    ans = 0
    for i,high in enumerate(heights):
        while heights[stack[-1]] >high:
            h = heights[stack.pop()]
            w = i -stack[-1] - 1
            ans = max(ans, w*h)
        stack.append(i)
    return ans
