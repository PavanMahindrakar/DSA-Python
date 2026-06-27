class Solution():
    def revserse(self, n):
        revNum = 0
        while n > 0:
            lastDigit = n % 10
            revNum = (revNum * 10) + lastDigit
            n = n // 10

        return revNum

sol = Solution()
s = sol.revserse(7789)
print(s)
