class Solution:
    def numberToWords(self, num: int) -> str:
        # the idea is to convert the number to words using recursion
        # we can use a dictionary to map the numbers to words
        lessThanTen = {
            0: "", 1: "One", 2: "Two", 3: "Three", 4: "Four",
            5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"
        }
        lessThenTwenty = {
            10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
            14: "Fourteen", 15: "Fifteen", 16: "Sixteen", 17: "Seventeen",
            18: "Eighteen", 19: "Nineteen"
        }
        lessThanHundred = {
            1: "Ten", 2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty",
            6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninety"
        }
        # starting from the atomic base case
        # and then moving to the higher order
        def solve(num: int) -> str:
            if num < 10:
                return lessThanTen[num].strip() 
            elif num < 20:
                return lessThenTwenty[num].strip()
            elif num < 100:
                return (lessThanHundred[num//10] + " " + solve(num % 10)).strip()
            elif num < 1000:
                return (lessThanTen[num // 100] + " Hundred " + solve(num % 100)).strip()
            elif num < 1000000:
                return (solve(num // 1000) + " Thousand " + solve(num % 1000)).strip()
            elif num < 1000000000:
                return (solve(num // 1000000) + " Million " + solve(num % 1000000)).strip()
            else:
                return solve(num // 1000000000) + " Billion " + solve(num % 1000000000)

        if num == 0:
            return "Zero"
        else:
            return  solve(num).strip()
        