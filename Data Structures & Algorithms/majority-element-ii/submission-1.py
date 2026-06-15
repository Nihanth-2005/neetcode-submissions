from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c1=c2=None
        ct1=ct2=0
        for num in nums:
            if num==c1:
                ct1+=1
            elif num==c2:
                ct2+=1
            elif ct1==0:
                c1=num
                ct1=1
            elif ct2==0:
                c2=num
                ct2=1
            else:
                ct1-=1
                ct2-=1
        
        res=[]
        if nums.count(c1)>len(nums)//3:
            res.append(c1)
        if c2!=c1 and nums.count(c2)>len(nums)//3:
            res.append(c2)
        return res