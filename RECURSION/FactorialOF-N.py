# Functional Recursion to find the factorial of a number
# This code defines a recursive function to calculate the factorial of a given positive integer.n.
# The function uses a base case where if n is 1, it returns 1.

def Factorial(n):
    if n == 1:
        return 1
    
    return n * Factorial(n - 1)

n = int(input("Enter a positive integer: "))
print(Factorial(n))