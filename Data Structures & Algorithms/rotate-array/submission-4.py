class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)

        k = k % n

        # 1. Reverse full array
        for i in range(n // 2):
            nums[i], nums[n - i - 1] = nums[n - i - 1], nums[i]

        # 2. Reverse first k elements
        for j in range(k // 2):
            nums[j], nums[k - j - 1] = nums[k - j - 1], nums[j]

        # 3. Reverse remaining elements
        for x in range((n - k) // 2):
            nums[x + k], nums[n - x - 1] = nums[n - x - 1], nums[x + k]