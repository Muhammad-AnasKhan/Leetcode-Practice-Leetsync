class Solution:
    def isPalindrome(self, s: str) -> bool:
        if(s.strip() == '' or len(s)==1): return True

        s = ([char for char in s.lower() if char.isalnum()])
        # comparing reverse 
        return s == s[::-1]

        # 2 pointers aproach
        # s = ''.join([char for char in s.lower() if char.isalnum()])
        # if(s.strip() == '' or len(s)==1): return True
        # if s:
        #     l =0
        #     r = len(s)-1

        #     if s[l] != s[r]: 
        #         return False

        #     while (l<r):
        #         if s[l] == s[r]:
        #             l = l+1
        #             r = r-1
        #         else:
        #             return False
        #     return True
        # else:
        #     return False