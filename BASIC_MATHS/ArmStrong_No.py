n = int(input("Enter a number: "))
dup = n
sum = 0
while n > 0:
    last_digit = n % 10
    sum += last_digit ** 3
    n = n // 10

if dup == sum:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# Time complexity: O(n)