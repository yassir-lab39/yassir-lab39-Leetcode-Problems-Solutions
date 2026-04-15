class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        m , n = len(board), len(board[0])
        alive = 0
        copy = [[0 for _ in range(n+2)] for _ in range(m+2)]
        for i in range(1,m+1) : 
            for j in range(1,n+1) :
                copy[i][j] = board[i-1][j-1]
        for i in range(1,m+1) :
            for j in range(1,n+1) :
                alive = copy[i-1][j-1]+copy[i-1][j]+copy[i-1][j+1]+copy[i][j-1]+copy[i][j+1]+copy[i+1][j-1]+copy[i+1][j]+copy[i+1][j+1]
                if copy[i][j] == 1 :
                    if alive < 2 or alive > 3 :
                        board[i-1][j-1] = 0
                else :
                    if alive == 3 :
                        board[i-1][j-1] = 1
                alive = 0


        
