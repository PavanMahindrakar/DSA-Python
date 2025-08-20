#1. using Sum formula
class Solution:
    def missingValue(self, arr):
        n = len(arr)
        total_sum = n * (n + 1) // 2   # use integer division
        s2 = 0

        for i in range(n - 1):
            s2 += arr[i]

        return total_sum - s2


# Example usage
arr = [1, 2, 3, 5]
sol = Solution()
print("Missing value:", sol.missingValue(arr))



#2. using XOR

class Solution:
    def missingValue(self, arr):
        n = len(arr)
        xor1 = 0   # XOR of numbers from 1 to n
        xor2 = 0   # XOR of elements in the array

        for i in range(n - 1):
            xor2 ^= arr[i]      # XOR of elements in array
            xor1 ^= (i + 1)     # XOR of numbers from 1 to n

        xor1 ^= n   # include last number (n)

        return xor1 ^ xor2


# Example usage
arr = [1, 2, 3, 5, 6]
sol = Solution()
print("Missing value:", sol.missingValue(arr))
