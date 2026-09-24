class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        

        if len(s1) > len(s2):
            return False
        else:
            s1_freq = [0] * 26
            s2_freq = [0] * 26

            for ch in s1:
                s1_freq[ord(ch) - ord('a')] +=1 

            i = 0
            j = 0

            while j < len(s2):
                s2_freq[ord(s2[j]) - ord('a')] += 1

                if j - i + 1 > len(s1):
                    s2_freq[ord(s2[i]) - ord('a')] -=1
                    i+=1

                if s1_freq == s2_freq:
                    return True
                j+=1

            return False

                    

            

                

                

        
        