class Solution(object):
    def reverse(self, x):
        sign = -1 if x < 0 else 1
        result=0
        num = abs(x)
        while num > 0:
            rem = num % 10
            num = num // 10
            result = result * 10 + rem
        return result*sign if -2**31 <= result <= 2**31-1 else 0 