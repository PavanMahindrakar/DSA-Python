# Check if an array is sorted in non-decreasing order
# This solution uses a simple loop to achieve O(n) time complexity.
class solution:
    def isSorted(self,arr):
        n = len(arr)
        for i in range(1,n):
            if(arr[i]>= arr[i-1]):
                continue
            else:
                return False
            
        return True
    

#`Example usage:
arr = [1, 2, 3, 4, 5]
sol = solution()
print(sol.isSorted(arr))  # Output: True