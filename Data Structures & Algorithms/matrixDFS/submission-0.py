class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited = set()
        ROWS = len(grid)
        COLS = len(grid[0])
        return self.traverse(0,0,ROWS,COLS,visited,grid)


    def traverse(self, r, c, ROWS, COLS,visited, grid) -> int:
        
        # Back Tracking Case
        if (r < 0 or c < 0 or r == ROWS or c == COLS 
            or (r,c) in visited or grid[r][c] == 1):
            return 0
        
        if (r == ROWS - 1) and (c == COLS - 1):
            return 1

        visited.add((r,c))

        count = 0 

        count += self.traverse(r+1,c,ROWS,COLS,visited,grid)
        count += self.traverse(r-1,c,ROWS,COLS,visited,grid)
        count += self.traverse(r,c+1,ROWS,COLS,visited,grid)
        count += self.traverse(r,c-1,ROWS,COLS,visited,grid)

        visited.remove((r,c))

        return count

