# Approach No. 1 # Time Complexity: O(min(a, b))
def Greatest_common_divisor(a, b):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    for i in range(min(a, b), 0, -1):
        if a % i == 0 and b % i == 0:
            return i
        
    # print("GCD of", a, "and", b, "is:", Greatest_common_divisor(a, b))

# Time Complexity: O(min(a, b))
print(Greatest_common_divisor(0, 0))  # Initial call to start


# Approach No. 2 # Time Complexity: O(log(min(a, b)))
# Using Euclidean algorithm
# This is a more efficient method to find the GCD
def gcd(a, b):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    while a > 0 and b > 0:
        if a > b:
            a = a % b
        else:
            b = b % a

    if a == 0:
        return b
    return a

# Time Complexity: O(log(min(a, b)))
print(gcd(0, 0))  # Initial call to start