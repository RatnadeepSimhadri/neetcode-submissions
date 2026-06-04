class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dict = defaultdict(list)
        for str in strs: 
            key = "".join(sorted(str))
            anagram_dict[key].append(str)
        
        return list(anagram_dict.values())