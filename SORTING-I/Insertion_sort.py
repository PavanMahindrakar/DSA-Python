# Insertion Sort Algorithm Implementation
# This code implements the Insertion Sort algorithm to sort an array in ascending order.    
# time complexity: O(n^2) -- worst case
# optimized time complexity: O(n) in best case (if array is already sorted)

class Solution:
    def InsertionSor(self, arr):
        n = len(arr);
        for i in range(n):
            j = i;
            while j > 0 and arr[j-1] > arr[j]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
                j -= 1

        return arr
    

arr = list(map(int, input("Enter the array elements separated by space: ").split()))
sol = Solution()
sorted_arr = sol.InsertionSor(arr)
print("Sorted array:", sorted_arr)



