class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = -1 
        blue = len(nums)
        white = 0 

        while white < blue:
            if nums[white] == 0:
                red += 1
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
            elif nums[white] == 2:
                blue -= 1 
                nums[blue], nums[white] = nums[white], nums[blue]
            else:
                white += 1
        
