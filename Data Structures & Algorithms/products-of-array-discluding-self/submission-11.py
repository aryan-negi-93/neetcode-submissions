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

        arr = []
            
        for num in nums:
            if zero == 1:
                if num == 0:
                    arr.append(sums)
                else:
                    arr.append(0)
            else:
                arr.append(sums // num)

        return arr
            

        