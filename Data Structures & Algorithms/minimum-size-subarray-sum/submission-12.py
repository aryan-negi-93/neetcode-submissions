class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        i = 0
        j = 0

        sm = 0
        min_len = float('inf')

        while j < len(nums):
            sm += nums[j]

            while sm >= target:
                min_len = min(min_len , j - i + 1)
                sm-=nums[i]
                i+=1
            j+=1

        if min_len == float('inf'):
            return 0
        return min_len
        


            

    


