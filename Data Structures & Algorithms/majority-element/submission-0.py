class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        obj = {}

        for elm in nums:
            if elm not in obj:
                obj[elm] = 1
            else:
                obj[elm] += 1

        result = 0
        majority = 0
        for key , values in obj.items():
            if values > result:
                majority = key
                result = values
        return majority







        