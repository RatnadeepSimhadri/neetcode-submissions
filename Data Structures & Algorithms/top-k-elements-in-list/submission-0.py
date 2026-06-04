class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = Counter(nums)
        max_heap = []
        ans = []

        for key,value in dict(freq_counter).items():
            heapq.heappush(max_heap,(-value,key))
        
        for i in range(0,k):
            value,key = heapq.heappop(max_heap)
            ans.append(key)
        
        return ans

        