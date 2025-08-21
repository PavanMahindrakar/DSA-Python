# this is much better apprach than hashing
# time Complexity : O(n log n) + O(n/2 + 1)

class Solution:
    def SingleNumber(self, arr):
        freq = {}   # dictionary as map

        # Count frequencies
        for num in arr:
            freq[num] = freq.get(num, 0) + 1

        # Iterate like C++ for(auto it: mpp)
        for key, value in freq.items():
            if value == 1:
                return key

        return -1


# Example
arr = [1, 1, 2, 3, 3]
sol = Solution()
Single = sol.SingleNumber(arr)
print("Single number in the array:", Single)
