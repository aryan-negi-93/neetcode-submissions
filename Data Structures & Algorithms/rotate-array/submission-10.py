class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)

        if n < k:
            k = k % n

        for i in range(len(nums)//2):
            nums[i] , nums[n-i-1]  = nums[n-i-1] , nums[i] 

        for j in range(k//2):
            nums[j] , nums[k-j-1] = nums[k-j-1]  , nums[j]
      
        
        for x in range((n-k)//2):
            nums[x + k] , nums[n-x-1] = nums[n-x-1] , nums[x + k]

        return nums









        