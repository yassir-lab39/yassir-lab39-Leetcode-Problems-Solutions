class Solution:
    def neighbors(self, row: int, col: int, i: int, j: int):
        neighbors = set()
        if i-1 >= 0:
            neighbors.add((i-1,j))
        if i+1 < row:
            neighbors.add((i+1,j))
        if j-1 >= 0:
            neighbors.add((i,j-1))
        if j+1 < col:
            neighbors.add((i,j+1))
        return neighbors

    def bfs(self, i: int, j: int, board: List[List[str]]):
        q = [(i,j)]
        board[i][j] = "#"
        while q != []:
            node = q.pop(0)
            neighbors = self.neighbors(len(board), len(board[0]), node[0], node[1])
            for cell in neighbors:
                if board[cell[0]][cell[1]] == "O":
                    board[cell[0]][cell[1]] = "#"
                    q.append(cell)

    def solve(self, board: List[List[str]]) -> None:
        row = len(board)
        col = len(board[0])
        for j in range(col):
            if board[0][j] == "O":
                self.bfs(0,j,board)
        for j in range(col):
            if board[row-1][j] == "O":
                self.bfs(row-1,j,board)
        for i in range(row):
            if board[i][0] == "O":
                self.bfs(i,0,board)
        for i in range(row):
            if board[i][col-1] == "O":
                self.bfs(i,col-1,board)
        for i in range(row):
            for j in range(col):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "#":
                    board[i][j] = "O"          
        return board
