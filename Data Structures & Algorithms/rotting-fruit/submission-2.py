class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # To Start the Flow at Minute One Put all Rotten Fruits in a Quue
        # By Each Passing Minute the Next Fresh Fruits gets added to Rotten List 
        # Check Each neight if not already rotten. Add to Queue and mark rotten 

        R = len(grid)
        C = len(grid[0])
        rotten = deque()
        fresh = 0

        for r in range(0,R):
            for c in range(0,C):
                if grid[r][c] == 2:
                    rotten.append((r,c))
                if grid[r][c] == 1:
                    fresh += 1

        minutes = 0
        while rotten and fresh > 0: 
            size = len(rotten)
            for i in range(0,size):
                (r,c) = rotten.popleft()
                for neighbor in [(-1,0),(1,0),(0,1),(0,-1)]:
                    _r = r + neighbor[0]
                    _c = c + neighbor[1]
                    if 0 <= _r < R and 0 <= _c < C and grid[_r][_c] == 1:
                        rotten.append((_r,_c))
                        fresh -= 1
                        grid[_r][_c] = 2
            minutes += 1
        
        return minutes if fresh == 0 else -1

        



    