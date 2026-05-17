class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n


        prev_1 = 2
        prev_2 = 1
        for i in range(3,n+1):
            current = prev_1 + prev_2
            prev_2 = prev_1
            prev_1 = current

        
        return current