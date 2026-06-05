class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # similar to dummy node approach of linked lists merging (2)
        res=[]
        i,j=0,0
        while i<len(word1) and j<len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i+=1
            j+=1
        res.extend(word1[i:])
        res.extend(word2[j:])

        return "".join(res)
        