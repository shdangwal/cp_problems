class Solution:
    def romanToInt(self, s: str) -> int:
        num, pre = 0, ""
        for i in reversed(range(len(s))):
            if s[i] == "I" and (pre == "V" or pre == "X"):
                num -= 1
            elif s[i] == "X" and (pre == "L" or pre == "C"):
                num -= 10
            elif s[i] == "C" and (pre == "D" or pre == "M"):
                num -= 100
            elif s[i] == "I":
                num += 1
            elif s[i] == "V":
                num += 5
            elif s[i] == "X":
                num += 10
            elif s[i] == "L":
                num += 50
            elif s[i] == "C":
                num += 100
            elif s[i] == "D":
                num += 500
            elif s[i] == "M":
                num += 1000
            pre = s[i]
        return num
