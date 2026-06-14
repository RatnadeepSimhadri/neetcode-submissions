import copy
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        grid_copy = copy.deepcopy(grid)
        islands = 0 
        R = len(grid)
        C = len(grid[0])

        for r in range (0,R):
            for c in range(0,C):
                if grid_copy[r][c] == "1":
                    Solution.fill(grid_copy,r,c,R,C)
                    islands += 1

        return islands
        
    

    @staticmethod
    def fill(grid: List[List[str]], r: int, c:int, R: int, C:int ):
        grid[r][c] = "0"
        # Traverse all reachable neighbors and fill 
        for neighbor in [(-1,0),(1,0),(0,1),(0,-1)]:
            _r = r + neighbor[0]
            _c = c + neighbor[1]
            if 0 <= _r < R and 0 <= _c < C and grid[_r][_c] == "1":
                Solution.fill(grid,_r,_c, R, C)





       