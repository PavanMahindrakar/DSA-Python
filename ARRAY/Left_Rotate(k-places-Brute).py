def rotate_to_left(arr, k):
    n = len(arr)
    if n == 0:
        return arr

    k = k % n  # handle case when k > n

    # Step 1: store first k elements
    temp = arr[:k]

    # Step 2: shift remaining elements left
    for i in range(n - k):
        arr[i] = arr[i + k]

    # Step 3: copy temp elements at the end
    for i in range(n - k, n):
        arr[i] = temp[i - (n - k)]

    return arr


# Driver code
arr = [1, 2, 3, 4, 5, 6, 7]
k = 2
rotated = rotate_to_left(arr, k)
print("After Rotating the elements to left:")
print(rotated)
