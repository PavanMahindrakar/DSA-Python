# this is the brute force apprach using linear search to solve SingleNumber problem.
# Time Complexity: O(n2)
# Spcae Complexity: O(1)

class Solution:
    def SingleNumber(self,arr):
        n = len(arr)
        for i in range(n):
            num = arr[i]
            count = 0
            for j in range(n):
                if arr[j] == num:
                    count += 1
            

            if count == 1:
                return num
            
        

        return -1
    

##xample Solution
arr = [1 ,1 , 2, 3, 3]
sol=Solution()

Single = sol.SingleNumber(arr)
print("Single Number in the array:", Single)
