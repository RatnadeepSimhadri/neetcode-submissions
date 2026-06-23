from collections import defaultdict
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First Calculate the Frequency of Each number 
        counter = defaultdict(int)
        for num in nums:
            counter[num] += 1

        freq_bucket = [[] for i in range(len(nums)+1)] # Create Buckets and Collect based on frequency max bucket size len(array) if all elements are same

        for key,value in counter.items():
            freq_bucket[value].append(key)

        ans = []
        for indx in range(len(nums),-1,-1):
            bucket = freq_bucket[indx]
            if bucket:
                ans += bucket
            if len(ans) == k:
                break

        return ans