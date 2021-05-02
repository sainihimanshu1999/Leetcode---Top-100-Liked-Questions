def searchinamatrix(self,matrix):
    col,row=len(matrix[0]),0

    while col>=0 and row<len(matrix):
        if matrix[row][col]>target:
            col-=1

        elif matrix[row][col]<target:
            row+=1
        
        else:
            return True
    return False