class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        map = set()

        i = 0
        j = 0

        while j < len(nums):

            if abs(i + j) > k:
                map.remove(nums[i])
                i+=1
            
            if nums[j] in map:
                return True

            map.add(nums[j])
            j+=1

        return False



                








