# This code implements a recursive quick sort algorithm in Python.  
class QuickSort:
    @staticmethod
    def partition(nums, low, high):
        pivot = nums[low]
        i = low
        j = high
        while i < j:
            while i <= high - 1 and nums[i] <= pivot:
                i += 1
            while j >= low + 1 and nums[j] > pivot:
                j -= 1
            if i < j:
                nums[i], nums[j] = nums[j], nums[i]
        nums[low], nums[j] = nums[j], nums[low]
        return j

    @staticmethod
    def quick_sort_helper(nums, low, high):
        if low < high:
            p_index = QuickSort.partition(nums, low, high)
            QuickSort.quick_sort_helper(nums, low, p_index - 1)
            QuickSort.quick_sort_helper(nums, p_index + 1, high)

    @staticmethod
    def quick_sort(nums):
        QuickSort.quick_sort_helper(nums, 0, len(nums) - 1)
        return nums

# Example usage:
if __name__ == "__main__":  
    arr = [10, 7, 8, 9, 1, 5]
    sorted_arr = QuickSort.quick_sort(arr)
    print("Sorted array:", sorted_arr)