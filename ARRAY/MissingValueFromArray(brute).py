# this solution finds missing no. from array using linear search
# Time Complexity: O(n2)
# space complexity: O(1)

class Solution:
    def missingValueFromArray(self,arr):
        n = len(arr)
        for i in range(n):
            flag = 0

            for j in range(n-1):
                if arr[j]==i:
                    flag =1
                    break

            if flag == 0:
                return i
            

        return -1
    
# Example usage:

arr = [0, 1, 3, 4, 5]
sol = Solution()
missing = sol.missingValueFromArray(arr)
print(f"The missing value is: {missing}")
