class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = {}
        for num in nums:
            if num not in hashset:
                hashset[num]=1
            else:
                hashset[num]+=1
        for i,j in hashset.items():
            if j>1:
                return True
                exit(0)
        return False