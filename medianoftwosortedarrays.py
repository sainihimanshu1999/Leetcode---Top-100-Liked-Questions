def mediaoftwosortedarrays(self,A,B):
    C = A+B
    C.sort()

    n = len(C)

    if n%2==0:
        mid = int(n/2)
        median = (C[mid]+C[mid-1])/2
        return median
    
    else:
        mid = (n-1)/2
        median = int(mid)
        return C[median]