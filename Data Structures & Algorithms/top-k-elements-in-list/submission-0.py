class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap={}
        for i in nums:
            if i not in hashmap:
                hashmap[i]=1
            else:
                hashmap[i]+=1
        sorted_items=sorted(hashmap.items(),key=lambda x:x[1],reverse=True)
        res=[]
        for num,freq in sorted_items[:k]:
            res.append(num)
        return res