class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        _counter = [0] * 26 
        for _char in s:
            _counter[ord(_char) - ord('a')] += 1
        
        for _char in t: 
            _counter[ord(_char) - ord('a')] -= 1
            if _counter[ord(_char) - ord('a')] < 0:
                return False
        
        return True