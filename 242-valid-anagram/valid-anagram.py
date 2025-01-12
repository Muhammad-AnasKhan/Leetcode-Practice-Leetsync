class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # using sorting
        # return sorted(s) == sorted(t)

        # using hashset(tracking count for better efficiency as compared to sorting)
        #  We can use 2 hashsets to keep count and then compare them
        #  We can also use one hashset to ++ and -- the count of each character

        counter = {}
        for i in s:
            counter[i] = counter.get(i,0)+1
        for j in t:
            if j not in counter or counter[j] == 0:
                return False
            counter[j] -=1

        return True
        