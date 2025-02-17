class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # without using split
    
        # the idea is to start from the end of the string and count the length of
        # the last word
        lastWordStarted = False
        count = 0
        for i in reversed(s):
            if i != ' ':
                lastWordStarted = True
                count += 1
            elif lastWordStarted:
                break
        return count
