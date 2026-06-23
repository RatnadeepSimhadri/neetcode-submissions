from typing import List


class Solution:
    """
    Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

    Each product is guaranteed to fit in a 32-bit integer.

    Follow-up: Could you solve it in
    O(n)
    O(n) time without using the division operation?

    Input: nums = [1,2,4,6]
    Output: [48,24,12,8]

    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            raise ValueError()
        left_p = [1] * len(nums)
        """
        nums = [1,2,4,6]
        left_p = [1,1,2,8]
        """
        for i in range(1, len(nums)):
            left_p[i] = left_p[i - 1] * nums[i - 1]

        rr_product = 1 # Running Right Product
        ans = [0] * len(nums)
        for i in range(len(nums)- 1,-1,-1):
             ans[i] = left_p[i] * rr_product
             rr_product *= nums[i]

        return ans
