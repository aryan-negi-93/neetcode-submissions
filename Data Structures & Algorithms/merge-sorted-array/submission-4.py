class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        i = 0
        while i < len(nums1):
            if i >= m:
                nums1.pop(i)
                i-=1
            i+=1

        nums1.extend(nums2)

        nums1.sort()
        

        

        



        # for elm in nums2:
        #     nums1.append(elm)

        # nums1.sort()

        # val = m + n

        

        
            
        
        

        