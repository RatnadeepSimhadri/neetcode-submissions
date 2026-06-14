class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        if grid[0][0] == 1:
            return -1

        q = deque()
        visited = set()

        visited.add((0,0))
        q.append((0,0))

        level = 1

        while q:
            size = len(q)
            for i in range(0,size):
                (r,c) = q.popleft()
                if r == ROWS-1 and c == COLS - 1: # Terminal Node
                    return level
                for n in [(-1,0),(1,0),(0,1),(0,-1),(-1,-1),(-1,1),(1,-1),(1,1)]:
                    _r = r + n[0]
                    _c = c + n[1]
                    if  0 <= _r < ROWS and 0 <= _c < COLS and (_r,_c) not in visited and grid[_r][_c] == 0:
                        q.append((_r,_c))
                        visited.add((_r,_c))
            level += 1
        
        return -1