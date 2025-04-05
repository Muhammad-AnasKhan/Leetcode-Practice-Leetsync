class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        if n == 1: return True
        # x = 1
        ## using loop
        # while x<=n:
        #     if x == n:
        #         return True
        #     if x > n //3: # optimized to skip extra iteration
        #         break 
        #     x = x*3
        # return False

        # recursive
        # if n%3 !=0 : return False
        # return  self.isPowerOfThree(n//3)

        # additional follow up case: without loop & recursion
        # 32 bit signed int calculation ~ 1162261467 <= 2^31 - 1 = 2147483647
        if (1162261467 % n) == 0: 
            return True
        return False
        