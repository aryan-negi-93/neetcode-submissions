class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        arr = []

        for x in range(len(nums)):
            i = x+1
            j = len(nums) -1

            while i < j:
                total = nums[x] + nums[i] + nums[j]
                if total == 0:
                    if [nums[x] , nums[i] , nums[j]] not in arr:
                        arr.append([nums[x] , nums[i] , nums[j]])
                    i+=1
                    j-=1
                elif total > 0:
                    j-=1
                elif total < 0:
                    i+=1

        return arr
                
                

        



        