# Approach No. 1   #Time Complexity: O(n)
class Solution():
    def CountDigits(self, n):
        cnt = 0
        while(n > 0):
            lastdigit = n % 10
            cnt += 1
            n = n // 10

        return cnt
    
sol = Solution()
print(sol.CountDigits(7789))