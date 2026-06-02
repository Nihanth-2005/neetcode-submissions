class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        #Brute Force or general approach
        # seen={}
        # max_count=0
        # for i in nums:
        #     if i in seen:
        #         seen[i]+=1
        #         if seen[i]>max_count:
        #             max_count=seen[i]
        #     else:
        #         seen[i]=1
        # for k,v in seen.items():
        #     if v==max_count:
        #         return k

        # boyer - moore algorithm
        candidate=None
        count=0
        for num in nums:
            if count==0:
                candidate = num
            if candidate==num:
                count+=1
            else:
                count-=1
        return candidate