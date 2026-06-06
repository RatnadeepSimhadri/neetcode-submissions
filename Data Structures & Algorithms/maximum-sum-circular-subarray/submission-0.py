class Solution:
    def maxSubarraySumCircular(self, nums: list[int]) -> int:
        if not nums:
            return 0
        globalMaxSum = nums[0]
        globalMinSum = nums[0]
        currentMaxSum = 0
        currentMinSum = 0
        total = 0
        for num in nums:
            total += num
            currentMaxSum = max(currentMaxSum + num,num)
            currentMinSum = min(currentMinSum + num,num)
            globalMaxSum = max(globalMaxSum, currentMaxSum)
            globalMinSum = min(globalMinSum, currentMinSum)

        return max(globalMaxSum, (total - globalMinSum)) if globalMaxSum > 0 else globalMaxSum