# Remove Duplicates from an array using brute force method
# This solution uses a set to achieve O(n) time complexity and O(n) space complexity
class Solution:
    def removeDuplicates(self,arr):
        sets = set()
        n = len(arr)
        for i in range(n):
            sets.add(arr[i])

        index = 0
        for item in sets:
            arr[index] = item
            index += 1  

        return index  # Return the new length of the array without duplicates
    
# Example usage:
arr = [1, 2, 2, 3, 4, 4, 5]
print("Before Removing Duplicates", arr)
sol = Solution()
print(sol.removeDuplicates(arr))  # Output: 5
print("After Removing Duplicates",arr[:5])  # Output: [1, 2, 3,4, 5]