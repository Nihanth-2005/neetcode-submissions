from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        n=len(nums)
        oplst=[]
        for key,value in count.items():
            if value>(n/3):
                oplst.append(key)

        return oplst