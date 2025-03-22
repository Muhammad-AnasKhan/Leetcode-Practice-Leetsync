class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        # brute force 0(n)
        # peak = 0
        # for i in range(1, len(arr)):
        #     if arr[i] > arr[peak]:
        #         peak = i
        # return peak

        # optimal solution
        # the idea is to use binary search
        # we can find the peak element in O(log n) time
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2
            if arr[mid] < arr[mid + 1]: # move right
                left = mid + 1 # we can discard the lower point
            else: # move left
                right = mid
        return left