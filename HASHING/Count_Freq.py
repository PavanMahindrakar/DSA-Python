# Count Frequencies of Elements in an Array
# This code defines a class Solution with a method countFrequencies that counts the frequency of each element in a list of integers.
# It returns a list of lists, where each inner list contains an element and its frequency.

class Solution:
    def countFrequencies(self, nums):
        freq_map = {}

        # Count the frequency of each number
        for num in nums:
            if num in freq_map:
                freq_map[num] += 1
            else:
                freq_map[num] = 1

        # Prepare the result
        result = []
        for key, value in freq_map.items():
            result.append([key, value])

        return result

# Example usage:
if __name__ == "__main__":  
    solution = Solution()
    nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    frequencies = solution.countFrequencies(nums)
    print(frequencies)  # Output: [[1, 1], [2, 2], [3, 3], [4, 4]]