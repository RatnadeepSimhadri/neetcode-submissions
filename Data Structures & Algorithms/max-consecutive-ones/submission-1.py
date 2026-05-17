class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_number = -1
        current = 0
        for num in nums:
            if num == 1:
                current += 1
                 
            else:
                max_number = max(max_number,current)
                current = 0
        
        return max(max_number,current)