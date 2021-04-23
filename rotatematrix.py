'''
print the transpose of the matrix
'''

def transpose(self,matrix):
    matrix[:] = [[row[i] for row in matrix[::-1]] for i in range(len(matrix))]