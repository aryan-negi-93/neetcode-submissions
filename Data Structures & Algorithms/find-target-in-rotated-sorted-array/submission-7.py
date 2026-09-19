class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot_index = left

        left_arr = nums[:left+1]
        right_arr = nums[left:]

        # check in left side arr
        left = 0
        right = len(left_arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if left_arr[mid] == target:
                return mid
            elif left_arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1


        # check right side arr

        left = 0
        right = len(right_arr) - 1

        while left <= right:
            mid = (left + right) // 2

            if right_arr[mid] == target:
                return mid + pivot_index
            elif right_arr[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1

        



        