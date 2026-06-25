class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        '''
        nums=[1,2,3,4,5,6,7,8], k=3 
        ==> [8,1,2,3,4,5,6,7]
        ==> [7,8,1,2,3,4,5,6]
        ==> [6,7,8,1,2,3,4,5]
        '''
        n=len(nums)
        k=k%n
        def reverse(left,right):
            while left<right:
                nums[left],nums[right] = nums[right],nums[left]
                left+=1
                right-=1
        reverse(0,n-1)
        reverse(0,k-1)
        reverse(k,n-1)