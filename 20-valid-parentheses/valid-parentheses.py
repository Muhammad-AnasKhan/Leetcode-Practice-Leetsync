class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in "({[":
                stack.append(i) 
            elif i in "]})":
                if not stack:
                    return False
                if i == ')' and stack[-1] == '(':
                    stack.pop()
                elif i == '}' and stack[-1] == '{':
                    stack.pop()
                elif i == ']' and stack[-1] == '[':
                    stack.pop()
                else:
                    return False
        return not stack

        # stack = []
        # mapping = {")":"(", "}":"{", "]":"["}

        # for char in s:
        #     if char in mapping.values():
        #         stack.append(char)
        #     elif char in mapping.keys():
        #         if not stack or mapping[char] != stack.pop():
        #             return False
        
        # return not stack
        