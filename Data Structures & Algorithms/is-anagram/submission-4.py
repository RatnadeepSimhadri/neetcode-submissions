class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_map = [0] * 26
        for _char in s:
            freq_map[ord(_char) - ord("a")] += 1

        for _char in t:
            freq_map[ord(_char) - ord("a")] -= 1
            if freq_map[ord(_char) - ord("a")] < 0:
                return False

        return True