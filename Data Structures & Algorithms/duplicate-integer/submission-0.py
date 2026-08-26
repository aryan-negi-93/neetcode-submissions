class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        obj = {}

        for i in range(len(nums)):
            if nums[i] not in obj:
                obj[nums[i]] = 1
            else:
                return True
        return False
        