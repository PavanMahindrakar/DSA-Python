# This code finds the second largest element in an array using a brute force approach by sorting the array.
# It implements a function to find the second largest element in an array in Python.

class solution:
    def secLargest(self,arr):
        # sort the array first
        arr.sort()
        # return the second last element
        return arr[-2]
    

# Example usage:
sol = solution()    
arr = [10, 20, 4, 45, 99]
second_largest_element = sol.secLargest(arr)
print("Second largest element in the array is:", second_largest_element)