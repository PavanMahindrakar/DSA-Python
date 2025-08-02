# Fibonacci series using recursion
# This code generates the Fibonacci series up to a given number of terms using recursion.   

def fibo(n):
    if n <= 1:
        return n
    
    LastNumber = fibo(n-1)
    SecondLastNumber = fibo(n-2)
    return LastNumber + SecondLastNumber

n = int(input("Enter the number of terms in Fibonacci series: "))

print("Fibonacci series:", fibo(n))