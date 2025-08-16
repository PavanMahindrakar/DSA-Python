# Remove Duplicates from Sorted Array (Optimal Solution)
# This solution uses two pointers to achieve O(n) time complexity and O(1) space complexity.

class Solution:
    def removeDuplicates(self,arr):
        n = len(arr)
        i = 0;

        for j in range(n):
            if arr[j]!= arr[i]:
                arr[1++i] = arr[j]
                i+= 1

        
        return i + 1  # Return the new length of the array without duplicates
    


# Example usage:
arr = [1, 2, 2, 3, 4, 4, 5]
print("Before Removing Duplicates", arr)
sol = Solution()
print(sol.removeDuplicates(arr))  # Output: 5
print("After Removing Duplicates", arr[:5])  # Output: [1, 2, 3, 4, 5]