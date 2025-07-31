# Approach 1 # Time Complexity: O(n)
n = int(input("Enter a number: "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count += 1

if count == 2:
    print("Prime")
else:
    print("Not Prime")


# Approach 2 # Time Complexity: O(sqrt(n))
import math
def is_prime():
    n = int(input("Enter a number: "))
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1
            if n // i != i:
                count += 1
        
    if count == 2:
        print("Prime")
    else:
        print("Not Prime")

is_prime()