# using backtracking to print numbers from 1 to N
# Time Complexity: O(n)

def ONE_To_N(i,n):
    if i < 1:
        return
    ONE_To_N(i - 1, n)
    print(i)

n = int(input("Number of times: "))
ONE_To_N(n, n)
        