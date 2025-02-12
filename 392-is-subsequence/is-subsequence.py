class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # for brute force solution, we can iterate thorugh the (larger) string t and check if the string s is a subsequence of t

        # for optimized solution
        # the idea is to use two pointers and check if the string s is a subsequence of t
        # using fast and slow pointer
        s_pointer = t_pointer = 0
        while (t_pointer<len(t) and s_pointer < len(s)):
            if t[t_pointer] == s[s_pointer]:
                s_pointer += 1
            t_pointer += 1
        return s_pointer == len(s)
            