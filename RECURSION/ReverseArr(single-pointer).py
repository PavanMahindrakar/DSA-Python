# Reverse an array using recursion with a single pointer
# The function revArr takes an array and an index i, and recursively swaps the elements at  # index i and the corresponding index from the end of the array until the entire array is reversed.

def revArr(arr, i):
    if i >= len(arr) // 2:
        return
    # Swap the elements at indices i and len(arr) - 1 - i
    arr[i], arr[len(arr) - 1 - i] = arr[len(arr) - 1 - i], arr[i]
    
    revArr(arr, i + 1)

n = int(input("Enter the number of elements in the array: "))
Array = input("Enter the elements of the array separated by spaces: ").split()
revArr(Array, 0)
print("Reversed array:", ' '.join(Array))   