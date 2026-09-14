class Solution:
    def isValid(self, s: str) -> bool:

        if s[0] in "}])":
            return False


        stack = []
        mapping = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for ch in s:
            if ch in "([{":
                stack.append(ch)
            else:
                if not stack:
                    return False
                if mapping[ch] != stack[-1]:
                    return False
                else:
                    stack.pop()
        
        if stack:
            return False
        return True