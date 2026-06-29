class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        find=0
        for i in range(1,n+1):
            find ^= i
        for i in nums:
            find ^= i
        return find