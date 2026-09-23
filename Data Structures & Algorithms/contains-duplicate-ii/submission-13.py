class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        st = set()

        i = 0
        j = 0

        while i < len(nums) and j < len(nums):
            if j - i <= k:
                if nums[j] in st:
                    return True
                else:
                    st.add(nums[j])
                    j+=1
            else:
                st.remove(nums[i])
                i+=1
            

        return False
        
        