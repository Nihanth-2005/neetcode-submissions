import string
from string import whitespace, punctuation
class Solution:
    def isPalindrome(self, s: str) -> bool:
        i,j=0,len(s)-1
        #"  No Lemon, no melon"
        if len(set(s))==1:
            return True
        while i<j:
            while i<j and not s[i].isalnum():
                i+=1
            while i<j and not s[j].isalnum():
                j-=1
            
            if s[i].lower()!=s[j].lower():
                return False
            i+=1
            j-=1
        return True