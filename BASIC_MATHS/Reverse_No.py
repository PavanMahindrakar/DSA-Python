# Approach   # Time Complexity: O(n)
n = int(input("Enter a number: "))

revNumber = 0
while n > 0:
    last_digit = n % 10
    revNumber = revNumber * 10 + last_digit
    n = n // 10

print("Reversed number:", revNumber)


