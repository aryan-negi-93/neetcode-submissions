class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        k = len(s1)
        i = 0

        while i + k <= len(s2):

            window = s2[i:i+k]

            if sorted(window) == sorted(s1):
                return True

            i += 1

        return False