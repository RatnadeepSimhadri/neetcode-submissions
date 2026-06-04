class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = dict(Counter(nums))
        freq = [(num,freq) for num,freq in freq_map.items()]
        freq.sort(key= lambda x: -x[1])
        ans = []
        for i in range(0,k):
            ans.append(freq[i][0])
        return ans


        