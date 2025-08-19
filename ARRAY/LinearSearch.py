# Linear Search Implementation
# This code defines a class Solution with a method LinearSearch that performs a linear search on an array to find the index of a target element.

class Solution:
    def LinearSearch(self, arr, target):
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1
    

# Example usage
n = 5
arr = [4, 2, 3, 1, 5]
target = 3
solution = Solution()
result = solution.LinearSearch(arr, target)
print("Index of target element:", result)  # Output: Index of target element: 2
