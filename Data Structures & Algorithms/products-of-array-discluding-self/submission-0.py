class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_to_right = [1] * len(nums)
        for index in range(len(nums)-2,-1,-1):
            product_to_right[index] = nums[index+1] * product_to_right[index+1]
        
        ans = [1] * len(nums)
        running_product = 1
        for i in range(len(nums)):
            ans[i] = running_product * product_to_right[i]
            running_product *= nums[i]
        
        return ans