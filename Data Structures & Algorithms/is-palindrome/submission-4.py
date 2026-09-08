class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        res = ""
        for elm in s:
            if elm.isalnum():
                res+=elm

        print(res)

        return res == res[::-1]




        