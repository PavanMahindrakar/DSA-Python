# Bubble Sort Implementation
# This code implements the Bubble Sort algorithm to sort an array in ascending order.   
# time complexity: O(n^2) -- worst case
# optimized time complexity: O(n) in best case (if array is in ascending order)

class Solution:
    def BubbleSort(self,arr):
        n = len(arr)
        for i in range(n-1, -1, -1):
            didSwap = 0
            for j in range(i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    didSwap = 1

            if didSwap == 0:
                break

            print("runs\n")
        return arr
    


#Example usage:
sol = Solution()
arr = input("Enter the array elements separated by space: ").split()
sorted_arr = sol.BubbleSort(arr)
print("Sorted array:", sorted_arr)