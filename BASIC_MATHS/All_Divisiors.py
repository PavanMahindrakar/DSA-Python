#print all divisors of a number
# Approach 1  # Time Complexity: O(n)
n = int(input("Enter a number: "))

def all_divisors(n):
    divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            divisors.append(i)
    return divisors

print("All divisors of", n, "are:", all_divisors(n))


# Approach 2  # Time Complexity: O(sqrt(n))
import math
def all_divisors_sqrt(n):
    divisors = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # Avoid adding the square root twice
                divisors.append(n // i)
    return sorted(divisors)

n = int(input("Enter a number: "))
print("All divisors of", n, "are:", all_divisors_sqrt(n))