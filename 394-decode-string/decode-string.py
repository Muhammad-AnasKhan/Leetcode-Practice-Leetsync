class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for i in s:
            if i != ']':
                stack.append(i)
            else:
                # substring retrieval
                substring = ''
                while stack[-1] != '[':
                    substring = stack.pop() + substring
                stack.pop() # pop the [

                # k retrieval
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                # multiply the decoded substring
                # for j in range(int(k)):
                #     res = ''
                #     res += substring

                # same as int(k) * substring
                
                stack.append(int(k) * substring)
        return "".join(stack)