# This code implements a recursive insertion sort algorithm in Python.
# time complexity: O(n^2) -- worst case
# space complexity: O(n) -- due to recursion stack
class Solution:
    def insertionSort(self, nums):
        def sort_recursive(n):
            # Base case: array of size 1 is already sorted
            if n <= 1:
                return
            
            # Sort first n-1 elements
            sort_recursive(n - 1)
            
            # Insert nth element into sorted part
            last = nums[n - 1]
            j = n - 2
            
            # Shift elements to make space for last
            while j >= 0 and nums[j] > last:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = last

        sort_recursive(len(nums))
        return nums


# Example usage
nums = [100, 90, 80, 70, 60, 50]
sol = Solution()
print(sol.insertionSort(nums))
