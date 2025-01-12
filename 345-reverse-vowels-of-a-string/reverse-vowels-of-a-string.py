class Solution:
    def reverseVowels(self, s: str) -> str:
        # using 2 pointers
        s_list = list(s)
        l =0
        r = len(s)-1
        vowels = 'aeiou'
        while (l<r):
            if s[l].lower() in vowels and s[r].lower() in vowels:
                temp = s[l]
                s_list[l] = s_list[r]
                s_list[r] = temp

                l = l+1
                r = r-1
            if s[l].lower() not in vowels:
                l = l+1

            if s[r].lower() not in vowels:
                r = r-1
        return ''.join(s_list)
        