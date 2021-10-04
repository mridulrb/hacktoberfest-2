class Solution:
    # Complete this function
    # Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self, arr, N):
        max_so_far = 0
        max_here = 0

        for i in range(len(arr)):
            max_so_far += arr[i]
            max_so_far = max(max_so_far, 0)
            if max_so_far > max_here:
                max_here = max_so_far
        if max_here != 0 and max_so_far >= 0:
            return max_here

        arr.sort()
        return arr[N - 1]


def main():
    t = int(input())
    while t > 0:
        n = int(input())

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr, n))

        t -= 1
