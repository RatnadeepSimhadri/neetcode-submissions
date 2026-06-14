class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        R = len(grid) - 1
        C = len(grid[0]) - 1
        visited = set()
        counter = [0]
        if grid[0][0] == 1:
            return 0
        self.visit(grid,counter,0,0,visited)
        return counter[0]


    def visit(self,grid: List[List[int]], counter: List[int], r:int, c: int, visited: set[tuple]):
        
        visited.add((r,c))

        if r == len(grid) -1  and c == len(grid[0]) - 1:
            counter[0] += 1
        else:
            # Check all unvisited neighbors and visit
            for neighbors in [(1,0),(-1,0),(0,1),(0,-1)]:
                _r = r + neighbors[0]
                _c = c + neighbors[1]
                if (_r,_c) not in visited and 0 <= _r < len(grid) and 0 <= _c < len(grid[0]) and grid[_r][_c] != 1:
                    self.visit(grid,counter,_r,_c,visited)

        visited.remove((r,c))

