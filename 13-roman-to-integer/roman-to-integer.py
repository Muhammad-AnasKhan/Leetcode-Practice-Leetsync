class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {
        "I" : 1,
        "V": 5,
        "X" : 10,
        "L" : 50,
        "C" : 100,
        "D" : 500,
        "M" : 1000    
        }
        # the idea is to start from the last element and keep the sum 
        # comparing the current element with the next element

        # if the current element is less than the next element then subtract the current element from the sum

        sum = hashmap[s[-1]]

        for i in range(len(s)-2,-1,-1): # reverse loop
            if hashmap[s[i]] < hashmap[s[i+1]]:
                sum -= hashmap[s[i]]
            else:
                sum += hashmap[s[i]]
        return sum
        