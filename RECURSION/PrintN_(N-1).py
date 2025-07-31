# Print numbers from N to 1 using recursion
# Time Complexity: O(n)

def N_to_1(i,n):
    if i < 1:
        return
    print(i)
    N_to_1(i - 1, n)

n = int(input("Enter a number: "))
N_to_1(n, n)