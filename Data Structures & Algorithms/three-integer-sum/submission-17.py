class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        arr = []

        for x in range(len(nums)):
            i = x + 1
            j = n - 1
            while i < j:
                sm = nums[x] + nums[i] + nums[j]
                if sm == 0:
                    if [ nums[x] , nums[i] , nums[j] ] not in arr:
                       arr.append([ nums[x] , nums[i] , nums[j] ])
                    i+=1
                    j-=1
                elif sm > 0:
                    j-=1
                else:
                    i+=1
        return arr





                

        



        