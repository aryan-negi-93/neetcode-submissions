class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        
        result = [ None for _ in range(len(nums))]

        i = 0
        pos = 0
        neg = 1

        while i < len(nums):
            if nums[i] > 0:
                result[pos] = nums[i]
                pos+=2
                i+=1
            elif nums[i] < 0:
                result[neg] = nums[i]
                neg+=2
                i+=1

        return result

        

        
        
