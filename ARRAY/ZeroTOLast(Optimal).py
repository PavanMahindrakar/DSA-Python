class Solution:
    def ZeroTolast(seld,arr):
        j = -1
        n  = len(arr)
        for i in range(n):
            if arr[i] == 0:
                j = i
                break

        if j == -1:
            return arr
        
        for i in range(j + 1, n):
            if arr[i] != 0:
                arr[j], arr[i] = arr[i], arr[j]
                j += 1


        return arr
    
# Example usage
n = 5
arr = [0, 1, 0, 3, 12]
solution = Solution()
result = solution.ZeroTolast(arr)
print("Array After Moving Zeroes To the End:", result)  # Output: [1, 3, 12, 0, 0]