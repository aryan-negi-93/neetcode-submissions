class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        st = set()

        i = 0
        j = 0

        mx = 0
        count = 0

        while i < len(s) and j < len(s):
            if s[j] not in st:
                st.add(s[j])
                count+=1
                mx = max(mx , count)
                j+=1
            else:
                st.remove(s[i])
                count-=1
                i+=1

        return mx
            
                
            


