class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        [left,right] = self.slidingwindow(nums)
        return sum(nums[left:right+1])

    def slidingwindow(self, nums) -> list:
        maxLeft = maxRight = 0
        maxSum = float('-inf')
        currentSum = 0
        left = -1
        right = 0
        while right < len(nums):
            if currentSum <= 0:
                currentSum = nums[right]
                left = right

            else:
                currentSum += nums[right]

            if currentSum > maxSum:
                maxSum = max(currentSum,maxSum)
                maxLeft = left
                maxRight = right

            right += 1

        return [maxLeft,maxRight]