class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        obj = {}
        
        for num in nums:
            if num not in obj:
                obj[num] = 1
            else:
                obj[num] += 1

        arr = [key for key , value in obj.items() if value > len(nums) // 3 ]

        return arr



        


        