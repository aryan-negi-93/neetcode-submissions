class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr = 0
        map = {0: 1}

        for i in nums:
            curr += i

            if curr - k in map:
                res += map[curr - k]

            if curr in map:
                map[curr] += 1
            else:
                map[curr] = 1

        return res