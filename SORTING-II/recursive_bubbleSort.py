# This code implements a recursive bubble sort algorithm in Python.
# time complexity: O(n^2) -- worst case 
# space complexity: O(n) -- due to recursion stack

class Solution:
    def bubbleSort(self, nums):
        def helper(n):
            # base case: when array size is 1, stop
            if n == 1:
                return
            for i in range(n - 1):
                if nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
            helper(n - 1)  # recursive call on smaller part

        helper(len(nums))
        return nums


# Example usage
nums = [100, 90, 80, 70, 60, 50]
sol = Solution()
print(sol.bubbleSort(nums))
