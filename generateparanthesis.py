def generateparanthesis(self,n):
    result = []
    s = [('(',1,0)]

    while s:
        x,l,r = s.pop()
        if l-r<0 or l>n or r>n:
            continue
        if l==n and r==n:
            result.append(x)
        s.append((x+'(',l+1,r))
        s.append((x+')',l,r+1))
    return result