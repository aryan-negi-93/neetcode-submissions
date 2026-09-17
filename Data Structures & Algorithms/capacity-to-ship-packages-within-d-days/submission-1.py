class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        def check(weights, capacity, days):
            day = 1
            current_weight = 0

            for weight in weights:
                if current_weight + weight > capacity:
                    day += 1
                    current_weight = weight
                else:
                    current_weight += weight

            return day <= days


        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = (left + right) // 2

            if check(weights , mid , days):
                right = mid
            else:
                left = mid + 1

        return left

            












        