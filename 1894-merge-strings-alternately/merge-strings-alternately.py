class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ''
        len_word_1 = len(word1)
        len_word_2 = len(word2)
        longer_str = max(len_word_1,len_word_2)
        for i in range(longer_str):
            if i < len_word_1:
                s+=word1[i]
            if i < len_word_2:
                s+=word2[i]
        return s
        
