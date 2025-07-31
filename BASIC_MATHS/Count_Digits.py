# Approach No. 1   #Time Complexity: O(n)
input_number = input("Enter a number: ")
n = int(input_number)

count = 0
while n > 0:
    last_digit = n % 10
    count += 1
    n = n // 10

print("Number of digits:", count)


# Approach No. 2    # Time Complexity: O(log n)
from math import log10
n = int(input("Enter a number: "))
count = int(log10(n)+1)
print(count)