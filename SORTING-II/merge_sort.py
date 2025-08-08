# Merge Sort Implementation
# This code implements the Merge Sort algorithm to sort an array in ascending order.    
# time complexity: O(n log n) -- worst case

class Solution:
    def merge(self, arr, low, mid, high):
        temp = []
        left = low
        right = mid + 1

        while left <= mid and right <= high:
            if arr[left] <= arr[right]:
                temp.append(arr[left])
                left += 1
            else:
                temp.append(arr[right])
                right += 1

        while left <= mid:
            temp.append(arr[left])
            left += 1

        while right <= high:
            temp.append(arr[right])
            right += 1

        for i in range(low, high + 1):
            arr[i] = temp[i - low]

    def mergeSortHelper(self, arr, low, high):
        if low >= high:
            return
        mid = (low + high) // 2
        self.mergeSortHelper(arr, low, mid)
        self.mergeSortHelper(arr, mid + 1, high)
        self.merge(arr, low, mid, high)

    def mergeSort(self, nums):
        self.mergeSortHelper(nums, 0, len(nums) - 1)
        return nums


arr = list(map(int, input("Enter the array elements separated by space: ").split()))
sol = Solution()
sorted_arr = sol.mergeSort(arr)
print("Sorted array:", sorted_arr)