# This code finds the second largest element in an array using two passes.
# It implements a function to find the second largest element in an array in Python.
# This approach is more efficient than sorting the array.

class Solution:
    #first pass: find the largest element
    def secLargest(self, arr):
        largest = arr[0]
        for i in range(1, len(arr)):
            if arr[i] > largest:
                largest = arr[i]

        # second pass: find the second largest element
        second_largest = -1
        for i in range(len(arr)):
            if arr[i] > second_largest and arr[i] != largest:
                second_largest = arr[i]

        return second_largest
    
# Example usage:
sol = Solution()
arr = [10, 20, 4, 45, 99]
second_largest_element = sol.secLargest(arr)
print("Second largest element in the array is:", second_largest_element)