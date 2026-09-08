class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_no = min(nums)
        # print(len(nums))
        for i in range(len(nums)+2):
            if i not in nums and i != 0:
                print(i)
                return i
        