class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        R = len(grid) - 1
        C = len(grid[0]) - 1
        visited = set()
        counter = [0]
        if grid[0][0] == 1:
            return 0
        self.visit(grid,counter,0,0,R,C,visited)
        return counter[0]


    def visit(self,grid: List[List[int]], counter: List[int], r:int, c: int, R:int, C:int, visited: set[tuple]):
        
        visited.add((r,c))

        if r == R and c == C:
            counter[0] += 1
        else:
            # Check all unvisited neighbors and visit
            for neighbor in Solution.get_neighbors(r,c,R,C):
                if neighbor not in visited and grid[neighbor[0]][neighbor[1]] == 0: # not visited not blocked
                    self.visit(grid,counter,neighbor[0],neighbor[1],R,C,visited)

        visited.remove((r,c))
    



    @staticmethod
    def get_neighbors(r: int, c: int, R:int , C:int):
        neighbors = []
        DIRECTIONS = [[0,1],[0,-1],[1,0],[-1,0]]
        for _DIR in DIRECTIONS: 
            _r = r + _DIR[0]
            _c = c + _DIR[1]
            if _r >= 0 and _r <= R and _c >= 0 and _c <= C:
                neighbors.append((_r,_c))
        return neighbors

