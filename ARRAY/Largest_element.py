# Problem: Find the largest element in an array
# This code implements a function to find the largest element in an array in Python.

class Solution:
    def LargestElement(self,arr):
        Largest = arr[0];
        for i in range(1, len(arr)):
            if arr[i] > Largest:
                Largest = arr[i]
            
        return Largest
    

# Example usage:
sol = Solution()
arr = [10, 20, 4, 45, 99]
largest_element = sol.LargestElement(arr)
print("Largest element in the array is:", largest_element)