# Union of Sorted Arrays (Optimal)
# This code defines a class Solution with a method UnionOfSortedArrays that takes two sorted arrays and returns their union as a sorted array.
# Time Complexity: O(n1 + n2)
# Space Complexity: O(n1 + n2) for returning the union in a new array

class Solution:
    def UnionOfSortedArrays(self, arr1, arr2):
        n1 = len(arr1)
        n2 = len(arr2)
        i = 0
        j = 0

        union = []
        while i < n1 and j < n2:
            if arr1[i] <= arr2[j]:
                if not union or union[-1] != arr1[i]:
                    union.append(arr1[i])
                i += 1
            else:
                if not union or union[-1] != arr2[j]:
                    union.append(arr2[j])
                j += 1

        while i < n1:
            if not union or union[-1] != arr1[i]:
                union.append(arr1[i])
            i += 1

        while j < n2:
            if not union or union[-1] != arr2[j]:
                union.append(arr2[j])
            j += 1

        return union
    

# Example usage
n1 = 5
arr1 = [1, 3, 5, 7, 9]
n2 = 4
arr2 = [2, 4, 6, 8]
solution = Solution()
result = solution.UnionOfSortedArrays(arr1, arr2)
print("Union of Sorted Arrays:", result)  
# Output: Union of Sorted Arrays: [1, 2, 3, 4, 5, 6, 7, 8, 9]
