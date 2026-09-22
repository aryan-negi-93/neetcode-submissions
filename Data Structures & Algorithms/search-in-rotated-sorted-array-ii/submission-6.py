class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        def binarySearch(i,j,nums,target):
            while i <= j:
                mid = (i+j) // 2

                if nums[mid] == target:
                    return True
                elif nums[mid] > target:
                    j = mid - 1
                else:
                    i = mid + 1
            
            return False


        left = 0
        right = len(nums) -1 

        while left < right and nums[left] == nums[left+1]:
            left+=1
        
        while left < right and nums[right] == nums[right-1]:
            right-=1


        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot_index = left


        if binarySearch(0,pivot_index-1,nums , target):
            return True
        return binarySearch(pivot_index,  len(nums) -1 ,nums , target)





        
        