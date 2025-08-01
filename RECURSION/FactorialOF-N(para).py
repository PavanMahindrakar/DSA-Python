# parameterized recursion to calculate the factorial of a number

def Fact(i, factorial):
    if i < 1:
        print(factorial)
        return
    
    return Fact(i - 1, factorial * i)


n = int(input("Enter a positive integer: "))
# from 1 to n. It uses a base case where if n is 1, 
Fact(n, 1)