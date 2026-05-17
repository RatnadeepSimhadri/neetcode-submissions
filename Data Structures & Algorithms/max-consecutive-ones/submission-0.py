class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        current_streak =  0
        max_streak = 0
        for num in nums:
            if num != 1:
                max_streak = max(max_streak, current_streak)
                current_streak = 0
            else:
                current_streak+=1

        return max(current_streak,max_streak)