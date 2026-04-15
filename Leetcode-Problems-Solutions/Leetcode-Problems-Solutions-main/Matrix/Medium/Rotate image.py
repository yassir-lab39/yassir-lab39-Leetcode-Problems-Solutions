class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        i = 0
        while i < n//2 :
            copy = []
            for k in range(i,n-i) :
                copy.append(matrix[i][k])
            for k in range(i,n-i) :
                matrix[i][k] = matrix[n-k-1][i]
            for k in range(i,n-i) :
                matrix[k][i] = matrix[n-1-i][k]
            for k in range(i,n-i) :
                matrix[n-1-i][k] = matrix[n-k-1][n-1-i]
            for k in range(i,n-i) :
                matrix[k][n-1-i] = copy[k-i]
            i += 1
        

        
        
