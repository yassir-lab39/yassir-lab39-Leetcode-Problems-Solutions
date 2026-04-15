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
    
    def bfs(self, i: int, j: int, grid: List[List[int]]):
        q = [(i,j)]
        grid[i][j] = '#'
        while q != []:
            node = q.pop(0)
            neighbors = self.neighbors(len(grid), len(grid[0]), node[0], node[1])
            for cell in neighbors: 
                if grid[cell[0]][cell[1]] == '1':
                    grid[cell[0]][cell[1]] = '#'
                    q.append(cell)

    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])
        res = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == '1':
                    res += 1
                    self.bfs(i,j,grid)
        return res

            
