class Solution:
    def romanToInt(self, s: str) -> int:
        if len(s) > 15:
            return "Error"
        numerals = {
        "I": 1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
        total = 0
        for i in range(len(s) -1):
            if numerals[s[i]] < numerals[s[i+1]]:
                total -= numerals[s[i]]
            else:
                total += numerals[s[i]]
        return total + numerals[s[-1]]

# logic: We check string from left to right, if left char is less than right char, we - it from sum, else we add it to sum. , the loop runs till 1 char less from left to right, the last element is always added!