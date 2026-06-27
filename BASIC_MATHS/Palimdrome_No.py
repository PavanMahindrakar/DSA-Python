class Solution():
    def isPalindrome(self, n):
        if n < 0:
            return False
        
        dup = n
        rev = 0
        while n > 0:
            last_digit = n % 10
            rev = (rev * 10) + last_digit
            n = n // 10

        return dup == rev
    
# Example usage:
sol = Solution()
print(sol.isPalindrome(121))  # Output: True
print(sol.isPalindrome(-121)) # Output: False