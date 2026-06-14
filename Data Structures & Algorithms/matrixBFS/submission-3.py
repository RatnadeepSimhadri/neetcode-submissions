
class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        visited = set()
        queue = deque()
        ROWS = len(grid)
        COLS = len(grid[0])
        if grid[0][0] == 1:
            return -1

        visited.add((0,0))
        queue.append((0,0))
        
        level = 0 

        while queue:
            qsize = len(queue)
            for i in range(0,qsize):
                (r,c) = queue.popleft()
                if r == ROWS -1 and c == COLS - 1: # Found the Final Node 
                    return level
                for neighbor in [(-1,0),(1,0),(0,1),(0,-1)]:
                    _r = r + neighbor[0]
                    _c = c + neighbor[1]
                    if (_r,_c) not in visited and 0 <= _r < ROWS and 0 <= _c < COLS and grid[_r][_c] == 0:
                        visited.add((_r,_c))
                        queue.append((_r,_c))
            level += 1

        return -1
            




        
