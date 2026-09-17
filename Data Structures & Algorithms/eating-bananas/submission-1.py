class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def check(piles , mid , h):
            actual_hrs = 0
            for pile in piles:
                actual_hrs+=pile//mid

                if (pile%mid != 0):
                    actual_hrs+=1

            return actual_hrs <= h

        left = 1
        right = max(piles)

        while left < right:
            mid = (left + right) // 2

            if check(piles , mid , h):
                right = mid
            
            else:
                left = mid + 1

        return left

            








