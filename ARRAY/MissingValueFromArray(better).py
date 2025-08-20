class Solution:
    def miossingValueFromArray(self, arr):
        n = len(arr)   # size of array

        hash = [0] * (n + 2)   # mimic `hash[i+1] = {0}`

        # mark presence of each element
        for i in range(n):
            hash[arr[i]] = 1   # same logic as your code

        # check which value is missing
        for i in range(1, n + 2):   # search from 1 to n+1
            if hash[i] == 0:
                return i

        return -1


# Example usage
arr = [1, 2, 4, 5]
sol = Solution()
missing = sol.miossingValueFromArray(arr)
print("Missing value:", missing)
