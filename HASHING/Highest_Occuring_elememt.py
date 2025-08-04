class Solution:
    def mostFrequent(self, arr):
        from collections import defaultdict

        freq = defaultdict(int)

        # Count frequencies
        for num in arr:
            freq[num] += 1

        max_freq = 0
        result = float('inf')  # To ensure smallest element is chosen in case of tie

        # Find the element with max frequency and smallest value
        for num in freq:
            if freq[num] > max_freq or (freq[num] == max_freq and num < result):
                max_freq = freq[num]
                result = num

        return result

# Example usage:
if __name__ == "__main__":
    solution = Solution()
    arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    most_frequent = solution.mostFrequent(arr)
    print(most_frequent)  # Output: 4