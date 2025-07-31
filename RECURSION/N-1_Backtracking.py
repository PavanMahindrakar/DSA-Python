# backtracking approach to print numbers from N to 1
# Time Complexity: O(n)

def N_to_ONE(i):
    if i < 1:
        return
    print(i)
    N_to_ONE(i - 1)  # move toward base case

n = int(input("Enter a number: "))
N_to_ONE(n)
