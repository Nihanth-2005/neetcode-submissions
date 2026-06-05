class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # similar to dummy node approach of linked lists merging (2)
        new_str=""
        i,j=0,0
        for i in range(min(len(word1),len(word2))):
            new_str += word1[i]
            new_str += word2[j]
            i+=1
            j+=1
        if i!=len(word1):
            new_str += word1[i:]
        if j!=len(word2):
            new_str += word2[j:]
        return new_str
        