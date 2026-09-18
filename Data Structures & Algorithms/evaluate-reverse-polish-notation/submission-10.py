class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        result = 0

        for token in tokens:
            if token in ["+" , "-" , "*" , "/"]:

                b = stack.pop()
                a = stack.pop()
                

                if token == "+":
                    result = a + b
                elif token == "-":
                    result = a - b
                elif token == "*":
                    result = a*b
                elif token == "/":
                    result = int(a / b)
                
                stack.append(result)
                       
            else:
                stack.append(int(token))

        return stack[-1]




        

        