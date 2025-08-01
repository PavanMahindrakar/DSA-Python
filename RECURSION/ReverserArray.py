# Reverse an array using recursion
# The function ReverserArray takes an array and two indices L and R, and recursively swaps the elements at these indices until the entire array is reversed.
# The base case is when L is greater than or equal to R, at which point the function returns.
# The function modifies the array in place and does not return a new array.

def ReverserArray(arr, L, R):
    if L >=R:
        return
    
    # Swap the elements at indices L and R
    arr[R], arr[L] = arr[L], arr[R]
    ReverserArray(arr, L + 1, R - 1)


n = int(input("Enter the number of elements in the array: "))
Array = input("Enter the elements of the array separated by spaces: ").split()

ReverserArray(Array, 0, len(Array) - 1)
print("Reversed array:", ' '.join(Array))