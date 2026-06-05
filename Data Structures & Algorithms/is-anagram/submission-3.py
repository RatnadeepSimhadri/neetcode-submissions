class Solution:
    def isAnagram(self, s:str, t: str) -> bool:
        if len(s) != len(t):
            return False
        counter = [0] * 26
        for _char in s:
            counter[(ord(_char) - ord('a'))] += 1

        for _char in t:
            counter[(ord(_char) - ord('a'))] -= 1
            if  counter[(ord(_char) - ord('a'))] < 0:
                return False

        return True