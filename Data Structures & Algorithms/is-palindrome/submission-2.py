class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = ""
        for elm in s:
            if elm in "abcdefghijklmnopqrstuvwzyz1234567890":
                res+=elm

        print(res)

        return res == res[::-1]




        