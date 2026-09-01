class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans += str(len(s)) + "$" + s
        print(ans)
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0

        while i < len(s):

            j = i
            while s[j] != "$":
                j += 1

            l = int(s[i:j])

            start = j + 1
            end = start + l

            ans.append(s[start:end])

            i = end

        return ans
            
            
            
            

        

