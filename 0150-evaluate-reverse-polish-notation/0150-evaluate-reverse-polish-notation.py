class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numstack = []
        
        for i in tokens:
            if i == "+" or i == "-" or i == "/" or i == "*":
                num2 = numstack.pop()
                num1 = numstack.pop()
                if i == "+":
                    numstack.append(num1 + num2)
                elif i == "-":
                    numstack.append(num1 - num2)
                elif i == "*":
                    numstack.append(num1 * num2)
                else:
                    numstack.append(int(num1 / num2))
            else:
                numstack.append(int(i))
        
        return numstack[0]
                    
            