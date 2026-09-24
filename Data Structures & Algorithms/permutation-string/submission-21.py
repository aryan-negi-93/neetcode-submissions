class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        n = len(s1)
        m = len(s2)

        if n > m:
            return False

        s1_freq = [0] * 26
        s2_freq = [0] * 26

        for ch in s1:
            s1_freq[ord(ch) - ord('a')] += 1

        i = 0
        j = 0

        while j < m:

            s2_freq[ord(s2[j]) - ord('a')] += 1

            if j - i + 1 > n:
                s2_freq[ord(s2[i]) - ord('a')] -= 1
                i += 1

            if s1_freq == s2_freq:
                return True

            j += 1

        return False