class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = []
        columns = []
        for i in range(len(matrix)) :
            for j in range(len(matrix[0])) :
                if matrix[i][j] == 0 :
                    rows.append(i)
                    columns.append(j)
        for j in range(len(matrix[0])) :
            for i in range(len(rows)) :
                matrix[rows[i]][j] = 0   
        for i in range(len(matrix)) :
            for j in range(len(columns)) :
                matrix[i][columns[j]] = 0     
