class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for _str in strs:
            key = "".join(sorted(_str))
            anagrams[key].append(_str)
        
        return [ value for value in anagrams.values()]
