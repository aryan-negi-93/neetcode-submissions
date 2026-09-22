class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        if k == 0:
            return False

        i = 0
        j = 1

        while i < len(nums):

            while j < len(nums) and j - i <= k:
                if nums[i] == nums[j]:
                    return True
                j += 1

            i += 1
            j = i + 1

        return False

        