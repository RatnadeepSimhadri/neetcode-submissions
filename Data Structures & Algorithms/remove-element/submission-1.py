class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        right = len(nums)
        left = 0 
        while left < right:
            if nums[left] == val:
                right -= 1
                nums[right], nums[left] = nums[left], nums[right] # Swapping
            else:
                left+= 1

        return right
        