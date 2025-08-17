def reverse(arr, start, end):
    """Helper function to reverse array elements from start to end."""
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_left(arr, k):
    n = len(arr)
    k %= n   # handle case when k > n
    
    # Step 1: Reverse first k elements
    reverse(arr, 0, k - 1)
    # Step 2: Reverse last n-k elements
    reverse(arr, k, n - 1)
    # Step 3: Reverse whole array
    reverse(arr, 0, n - 1)

    return arr


# Driver code
arr = [1, 2, 3, 4, 5, 6, 7]
k = 2
rotated = rotate_left(arr, k)
print("After Rotating the k elements to left:", rotated)
