class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        set_map = set()

        i = 0
        j = 0

        while i < len(nums) and j < len(nums):
            if j - i <= k:
                if nums[j] in set_map:
                    return True
                    
                else:
                    set_map.add(nums[j])
                    j+=1
            else:
                set_map.remove(nums[i])
                i+=1

        return False





                








