class Solution:
    def shortestPath(self, grid: list[list[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()
        visited = set()

        queue.append((0,0))
        visited.add((0,0))
        distance = 0
        while queue:
            for i in range(len(queue)):
                (r,c) = queue.popleft()
                if r == ROWS - 1 and c == COLS - 1:
                    return distance
                neighbors = self.get_neighbors(r,c,ROWS,COLS,grid,visited)
                for (_r,_c) in neighbors:
                    queue.append((_r,_c))
                    visited.add((_r,_c))

            distance +=1

        return -1


    def get_neighbors(self,r,c,ROWS,COLS,grid: list[list[int]], visited):
        DIRS = [[1,0],[-1,0],[0,1],[0,-1]]
        neighbors = []
        for _dir in DIRS:
            _r = r + _dir[0]
            _c = c + _dir[1]
            if _r >=0 and _c >=0 and _r < ROWS and _c < COLS and grid[_r][_c] == 0 and (_r,_c) not in visited:
                neighbors.append((_r,_c))
        
        return neighbors
                

