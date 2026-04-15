class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        L = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(9) :
            for j in range(9) :
                if board[i][j] != "." :
                    if board[i][j] in L :
                        L.remove(board[i][j])
                    else :
                        return False
            L = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        for i in range(9) :
            for j in range(9) :
                if board[j][i] != "." :
                    if board[j][i] in L :
                        L.remove(board[j][i])
                    else :
                        return False
            L = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        i, j = 0, 0
        while i < 9 :
            while j < 9 :
                for k in range(i,i+3) :
                    for l in range(j, j+3) :
                        if board[k][l] != "." :
                            if board[k][l] in L :
                                L.remove(board[k][l])
                            else :
                                return False
                L = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                j += 3
            j = 0
            i += 3
        return True
