from math import ceil 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_f = 1 
        max_f = max(piles)

        while min_f < max_f:
            freq = (min_f + max_f) // 2
            if self.total_hours(freq,piles) <= h:
                max_f = freq
            else:
                min_f = freq+1

        return max_f

    

    def total_hours(self, freq: int, piles: List[int]):
        hours = 0 
        for pile in piles:
            hours += ceil(pile/freq)
        
        print(f"{freq}: {hours}")
        return hours