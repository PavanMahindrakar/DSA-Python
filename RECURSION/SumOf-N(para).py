# Parameterized recursion to calculate the sum of first N natural numbers from 1 to n.
# The function uses a base case where if n is 1,

def SumOF_N(i,sum):
    if i < 1:
        print(sum)
        return
    
    return SumOF_N(i - 1, sum + i)


n = int(input("Enter a positive integer: "))
SumOF_N(n, 0)