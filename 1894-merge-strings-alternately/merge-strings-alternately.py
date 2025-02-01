class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ''
        # len_word_1 = len(word1)
        # len_word_2 = len(word2)
        # longer_str = max(len_word_1,len_word_2)
        for i in range(max(len(word1),len(word2))):
            if i < len(word1):
                s+=word1[i]
            if i < len(word2):
                s+=word2[i]
        return s
        
