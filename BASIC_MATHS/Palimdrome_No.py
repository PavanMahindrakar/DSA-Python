n = int(input("Enter a number: "))
dup = n
revNumber = 0
while n > 0:
    last_digit = n % 10
    revNumber = revNumber * 10 + last_digit
    n = n // 10

if dup == revNumber:
    print("Palindrome")
else:
    print("Not Palindrome")


# time complexity: O(n)