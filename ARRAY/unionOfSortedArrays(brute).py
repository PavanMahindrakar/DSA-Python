# Union of Sorted Arrays (Brute Force Approach)
# This code defines a class Solution with a method UnionOfSortedArrays that takes two sorted arrays and returns their union as a sorted array.
# Time Complexity: O(n1 log n) + O(n2 log n) + O(n1 + n2) 
# Space Complexity: O(n1 + n2) for returning the union in a new array
class Solution:
    def UnionOfSortedArrays(self,arr1,arr2):
        n1 = len(arr1)
        n2 = len(arr2)

        set = []
        for i in range(n1):
            set.append(arr1[i])
        for i in range(n2):
            set.append(arr2[i])

        temp = []
        for i in set:
            temp.append(i)

        temp.sort()

        return temp
    
# Example usage
n1 = 5  
arr1 = [1, 3, 5, 7, 9]
n2 = 4
arr2 = [2, 4, 6, 8]
solution = Solution()
result = solution.UnionOfSortedArrays(arr1, arr2)
print("Union of Sorted Arrays:", result)  # Output: Union of Sorted Arrays: [1, 2, 3, 4, 5, 6, 7, 8, 9]