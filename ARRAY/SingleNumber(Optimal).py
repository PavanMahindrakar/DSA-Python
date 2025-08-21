# This is the most optimal apprach using XOR property
# time complexity : O(n)
# space complexity : O(1)
class Solution:
    def SingleNumber(self,arr):
        n = len(arr)
        XORR = 0
        for i in range(n):
            XORR = XORR ^ arr[i]


        return XORR
    

arr = [1 ,1 , 2, 3, 3]
sol=Solution()

Single = sol.SingleNumber(arr)
print("Single Number in the array:", Single)
