class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        good_index = -1
        
        for index, value in enumerate(nums):
            if value != val:
                good_index +=1
                nums[good_index] = nums[index]
        return good_index + 1
