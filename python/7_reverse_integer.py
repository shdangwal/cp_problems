class Solution:
    def reverse(self, x: int) -> int:
        if str(x)[0] == "-":
            val = int("-" + str(x)[len(str(x)) : 0 : -1])
            if val < -(2**31):
                return 0
            else:
                return val
        else:
            val = int(str(x)[::-1])
            if val > 2**31 - 1:
                return 0
            else:
                return int(str(x)[::-1])
