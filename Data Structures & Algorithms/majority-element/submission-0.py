class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Brute Force or general approach
        seen={}
        for i in nums:
            if i in seen:
                seen[i]+=1
            else:
                seen[i]=1
        j=max(seen.values())
        for k,v in seen.items():
            if v==j:
                return k