class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0: return False
        if n == 1: return True
        x = 1
        # using loop
        while x<=n:
            if x == n:
                return True
            if x > n //4: # optimized to skip extra iteration
                break 
            x = x*4
        return False

        # recursive
        # if n%4 !=0 : return False
        # return  self.isPowerOfThree(n//4)

        # additional case: without loop & recursion
        # 32 bit signed int calculation ~ 1073741824(4^15) <= 2^31 - 1 = 2147483647
        # if (1073741824 % n) == 0: 
        #     return True
        # return False