class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        counter = 0
        for elem in num_set:
            local_counter = 1
            current = elem - 1
            while current in num_set:
                  local_counter+=1
                  current -=1
            counter = max(counter,local_counter)
        
        return counter
