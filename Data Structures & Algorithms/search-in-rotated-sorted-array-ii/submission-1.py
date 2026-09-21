class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        def binary_search(l, r, nums, target):

            i = l
            j = r 

            while i <= j:
                mid = (i+j) // 2

                if nums[mid] == target:
                    return True
                elif nums[mid] < target:
                    i = mid + 1
                else:
                    j = mid - 1

            return False
        
        l = 0
        r = len(nums) -1
        while l < r and nums[l] == nums[l+1]:
            l+=1

        while l < r and nums[r] == nums[r-1]:
            r-=1

        
        while l < r:
            mid = (l + r) // 2

            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid

        pivot_index = l

        if binary_search(0, pivot_index - 1, nums, target):
            return True
        
        return binary_search(pivot_index, len(nums) - 1, nums, target)

        
    

        


                
            


        