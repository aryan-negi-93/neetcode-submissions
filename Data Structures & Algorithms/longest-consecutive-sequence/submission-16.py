class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

         set_nums = set(nums)
         longest = 0

         for num in nums:
            if num - 1 not in set_nums:
                curr = num
                count = 1

                while curr + 1 in set_nums:
                    count+=1
                    curr += 1

                longest = max(longest , count)

         return longest

        