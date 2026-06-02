class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Naive basic approach without follow up question
        n=len(nums)
        pref=[1]*n
        suff=[1]*n

        for i in range(1,n):
            pref[i] = nums[i-1] * pref[i-1]
        for i in range(n-2,-1,-1):
            suff[i] = nums[i+1] * suff[i+1]
        
        return [pref[i] * suff[i] for i in range(n)]