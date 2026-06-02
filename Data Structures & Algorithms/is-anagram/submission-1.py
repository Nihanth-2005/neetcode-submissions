class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            str1=sorted(s)
            str2=sorted(t)
            if str1==str2:
                return True
            return False