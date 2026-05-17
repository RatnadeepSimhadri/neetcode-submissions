# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        if not pairs:
            return []
        return self.mergeHelper(0,len(pairs)-1, pairs)

    def mergeHelper(self, start: int, end:int, pairs:List[Pair]):

        if end - start + 1 == 1:
            return pairs
        
        mid = (start+end) // 2

        self.mergeHelper(start,mid,pairs)
        self.mergeHelper(mid+1,end,pairs)

        left_start = start
        left_end = mid

        right_start = mid + 1
        right_end = end
        ans = [-1] * (end-start+1)
        index = 0
        while left_start <= left_end and right_start <= right_end:
            if pairs[left_start].key <= pairs[right_start].key:
                ans[index] = pairs[left_start]
                left_start +=1
                index += 1
            else:
                ans[index] = pairs[right_start]
                right_start += 1
                index += 1
        
        while left_start <= left_end:
            ans[index] = pairs[left_start]
            left_start +=1
            index += 1

        while right_start <= right_end:
            ans[index] = pairs[right_start]
            right_start += 1
            index += 1
        
        for index,pair in enumerate(ans):
            pairs[start] = pair
            start += 1
        return pairs



    
