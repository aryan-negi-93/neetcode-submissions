class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        k = len(s1)
        i = 0
        j = k

        while j <= len(s2):
            window = s2[i:j]

            if sorted(window) == s1:
                return True
            
            i+=1
            j+=1

        return False
