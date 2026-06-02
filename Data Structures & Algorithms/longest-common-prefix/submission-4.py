class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result=""
        for i in range(len(strs[0])):
            curr=strs[0][i]
            for word in strs:
                if i>=len(word) or word[i]!=curr:
                    return result
            result += curr
        return result