class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = {}

        # Frequency count
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        # Frequency ke according sort
        arr = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Top k elements
        result = []

        for i in range(k):
            result.append(arr[i][0])

        return result