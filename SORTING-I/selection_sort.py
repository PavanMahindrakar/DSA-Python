#Selection Sort Implementation
#This code implements the Selection Sort algorithm to sort an array in ascending order.    

#time complexity: O(n^2)

class Solution:
    def SelectionSort(self, arr):
        n = len(arr)
        for i in range(n-1):
            mini = i
            for j in range(i,n):
                if(arr[j]<arr[mini]):
                    mini = j

            arr[i], arr[mini] = arr[mini], arr[i]
        return arr
    

#Example usage:
sol = Solution()
arr = [64,25,10,70,30,40,20]

sorted_arr = sol.SelectionSort(arr)
print("Sorted array:", sorted_arr)