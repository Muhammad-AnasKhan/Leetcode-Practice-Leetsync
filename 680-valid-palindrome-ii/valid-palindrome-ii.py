class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) -1
        while(l<r):
            if s[l] != s[r]:#if we encounter unequal corresponding letters, try skipping any
                return self.isValidSubPalindrome(s, l + 1, r) or self.isValidSubPalindrome(s, l, r-1)
            
            l, r = l + 1, r -1
        return True
    # helper function to calcaulte sub palindrome
    def isValidSubPalindrome(self,s, l,r):
        while l < r:
            if s[l] != s[r]:
                return False
            l, r = l + 1, r -1
        return True