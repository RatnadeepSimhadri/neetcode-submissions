class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(int)
        max_freq = 0
        top = k
        ans = []
        for num in nums: 
            freq_map[num] += 1
            max_freq = max(max_freq, freq_map[num])
        
        buckets = [[] for _ in range(max_freq + 1)]

        for value, freq in freq_map.items():
            buckets[freq].append(value)
        
        for bucket in buckets[::-1]:
            for num in bucket:
                ans.append(num)
                top -= 1
                if top == 0:
                    break
        
        return ans[:k]




        