class Solution:
    def ZeroToLast(self,arr):
        n = len(arr)
        temp = []
        for i in range(n):
            if arr[i] != 0:
                temp.append(arr[i])

        NZ = len(temp)
        for i in range(NZ):
            arr[i] = temp[i]

        for i in range(NZ, n):
            arr[i] = 0


        return arr
    

# Example usage
n = 5
arr = [0, 1, 0, 3, 12]
solution = Solution()
result = solution.ZeroToLast(arr)
print("Array After Moving Zeroes To the End:",result)  # Output: [1, 3, 12, 0, 0]