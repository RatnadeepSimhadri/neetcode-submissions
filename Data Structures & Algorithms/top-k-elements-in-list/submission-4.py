class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        top = k
        ans = []
        for num in nums: 
            freq_map[num] += 1
        
        buckets = [[] for _ in range(len(nums) + 1)]

        for value, freq in freq_map.items():
            buckets[freq].append(value)
        
        for bucket in buckets[::-1]:
            for num in bucket:
                ans.append(num)
                if len(ans) == k:
                    return ans
        
        return []




        