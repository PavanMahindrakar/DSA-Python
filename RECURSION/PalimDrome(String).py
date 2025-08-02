# Palindrome Checker using Recursion
# This code checks if a given string is a palindrome using recursion.   
# A palindrome reads the same backward as forward, ignoring spaces, punctuation, and case.

class Solution:
    def isPalindromeRecursive(self, s: str) -> bool:
        # Clean the string by removing non-alphanumeric characters and converting to lowercase
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        
        # Helper function for recursion
        def checkPalindrome(left: int, right: int) -> bool:
            if left >= right:
                return True
            if cleaned[left] != cleaned[right]:
                return False
            return checkPalindrome(left + 1, right - 1)
        
        return checkPalindrome(0, len(cleaned) - 1)
    
    
isPalindrome = Solution()
# Example usage:
test_strings = [
    "A man, a plan, a canal: Panama",
    "racecar",
    "hello",
    "No lemon, no melon",
    "Was it a car or a cat I saw?"
]

for s in test_strings:
    result = isPalindrome.isPalindromeRecursive(s)
    print(f'"{s}" -> {result}')