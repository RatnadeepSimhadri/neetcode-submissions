class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        R = len(grid)
        C = len(grid[0])

        for r in range(0,R):
            for c in range(0,C):
                if grid[r][c] == 1:
                    area = Solution.parse(grid,r,c,R,C)
                    max_area = max(area, max_area)

        return max_area
                
        



    @staticmethod
    def parse(grid: List[List[int]], r: int, c:int, R:int, C:int) -> int:
        grid[r][c] = 0
        area = 1

        for neighbor in [(1,0),(-1,0),(0,1),(0,-1)]:
           _r = r + neighbor[0]
           _c = c + neighbor[1]
           if 0 <= _r < R and 0 <= _c < C and grid[_r][_c] == 1:
            area+= Solution.parse(grid,_r,_c,R,C)

        return area

