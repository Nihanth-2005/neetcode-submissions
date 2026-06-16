class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp={0:1}
        prefix,ans=0,0
        for num in nums:
            prefix+=num
            ans += mp.get(prefix-k,0)
            mp[prefix] = mp.get(prefix,0)+1
        return ans