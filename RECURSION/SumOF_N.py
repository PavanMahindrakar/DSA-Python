# This code calculates the sum of the first n natural numbers using recursion.
# The function SumOfN takes an integer n as input and returns the sum of all integers

def SumOfN(n):
    if n == 1:
        return 1
    return n + SumOfN(n - 1)  

n = int(input("Enter a positive integer: "))
print(SumOfN(n))
