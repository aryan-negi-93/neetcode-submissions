class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def check(weights , mid , days):
            day = 1
            curr_weight =0

            for weight in weights:
                if curr_weight + weight <= mid:
                    curr_weight += weight
                else:
                    day+=1
                    curr_weight = weight
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