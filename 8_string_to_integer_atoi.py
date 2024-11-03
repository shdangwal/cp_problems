class Solution:
    def myAtoi(self, s: str) -> int:
        num = ""
        mul = 0
        s = s.strip()
        for char in s:
            if (char == "-" or char == "+") and mul == 0 and num == "":
                mul = -1 if char == "-" else 1
            elif char.isdigit():
                num = num + char
            else:
                break

        if num == "":
            return 0
        if mul == 0:
            mul = 1
        num = int(num) * mul
        print("ij", num)
        if num > (2**31 - 1):
            return 2**31 - 1
        elif num < (-1 * 2**31):
            return -1 * 2**31
        return num
