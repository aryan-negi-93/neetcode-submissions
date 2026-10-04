class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        map = set()

        i = 0
        j = 0

        if k == 0:
            return False

        while j < len(nums):
            if abs(i - j) <= k:
                if nums[j] not in map:
                    map.add(nums[j])
                else:
                    return True
                j+=1
            else:
                map.remove(nums[i])
                i+=1
            

        return False
            



                








