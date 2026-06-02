class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """#Brute Force, TC: O(n^2)
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if i<j and (numbers[i]+numbers[j]== target):
                    return [i+1,j+1]
        """
        #Optimized
        n = len(numbers)
        left = 0
        right = n-1
        while left<right:
            if numbers[left] + numbers[right] > target:
                right-=1
            elif numbers[left] + numbers[right] < target:
                left+=1
            else:
                return [left+1, right+1]