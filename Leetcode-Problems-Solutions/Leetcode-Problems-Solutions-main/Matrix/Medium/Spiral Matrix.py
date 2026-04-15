class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        M = matrix
        L = []
        while len(M) > 1 and len(M[0]) > 1 :
            m = len(M)
            n = len(M[0])
            for j in range(n) :
                L.append(M[0][j])
            for i in range(1, m) :
                L.append(M[i][n-1])
            for j in range(n-2,-1,-1) :
                L.append(M[m-1][j])
            for i in range(m-2,0,-1) :
                L.append(M[i][0])
            M = [row[1:n-1] for row in M[1:m-1]]
        for i in range(len(M)) :
            for j in range(len(M[0])) :
                L.append(M[i][j])
        return L
            
            
