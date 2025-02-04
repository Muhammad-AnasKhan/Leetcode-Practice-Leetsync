class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        # Removing the first and last character from (s+s) helps avoid 
        # counting the trivial match when s aligns with itself at the boundaries. 
        # If s truly contains a repeated pattern,
        #  you'll still find s inside (s+s)[1:-1]. Otherwise, it won’t appear.
        
        return s in (s+s)[1:-1]