class Solution:
    def isValid(self, s: str) -> bool:

        

        stack = []

        mapping = {
            ")":"(",
            "}":"{",
            "]":"["
        }

        for elm in s:
            if elm in "([{":
                stack.append(elm)
            else:
                if not stack:
                    return False
                elif mapping[elm] != stack[-1]:
                    return False

                else:
                    stack.pop()

        if stack:
            return False
        return True


        