class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        zero = 0
        sums = 1

        for num in nums:
            if num == 0:
                zero+=1
            else:
                sums*=num
        
        if zero > 1:
            return [0 for _ in range(len(nums))]

        result = []

        for no in nums:
            if zero == 1:
                if no == 0:
                    result.append(sums)
                else:
                    result.append(0)
            else:
                result.append(sums // no)

        return result

        




            

        