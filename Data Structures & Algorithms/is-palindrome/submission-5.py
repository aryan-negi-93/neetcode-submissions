class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = ""
        for x in s:
            if x in "abcdefghijklmnopqstuvwxyz1234567890":
                res+=x

        return res == res[::-1]
        



        