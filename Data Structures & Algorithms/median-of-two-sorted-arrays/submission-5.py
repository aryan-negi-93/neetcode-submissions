class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:


        arr = nums1 + nums2
        arr.sort()

        if len(arr) % 2 == 0:
            mid = (0 + len(arr) ) // 2

            print(arr)

            print(arr[mid] , arr[mid-1])

            return (arr[mid] + arr[mid-1]) / 2
        else:
            mid = (0 + len(arr) ) // 2
            return arr[mid]


        















            






        
        