# this is the Better apprach using hashing 
# time complexity : O(3N)

class Solution:
    def SingleNumber(self,arr):
        n = len(arr)
        maximum = arr[0]
        for i in range(n):
            maximum = max(maximum,arr[i])

        hash = [0] * (maximum + 1)
        for i in range(n):
            hash[arr[i]] += 1

        for i in range(n):
            if hash[arr[i]] == 1:
                return arr[i]
            


        return -1
    

arr = [1,1,2,3,3]
sol= Solution()

Single = sol.SingleNumber(arr)
print("Single number in the array:", Single)