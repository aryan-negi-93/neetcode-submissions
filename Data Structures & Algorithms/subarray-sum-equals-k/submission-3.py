class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        curr = 0
        map = {0:1}

        for num in nums:
            curr+= num
            if curr - k in map:
                result += map[curr - k]
            
            if curr in map:
                map[curr] += 1
            else:
                map[curr] = 1

        return result
            




        