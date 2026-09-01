class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1


        arr = [ [] for _ in range(len(nums)+1)]

        result = []

        for key , value in freq.items():
            arr[value].append(key)


        for i in range(len(arr) - 1, -1, -1):
            result.extend(arr[i])

        return result[:k]

        

        
        


        

  