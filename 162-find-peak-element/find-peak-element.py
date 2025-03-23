class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # optimal solution
        # the idea is to use binary search
        # we can find the peak element in O(log n) time
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if  nums[mid] < nums[mid + 1]: # move right
                left = mid + 1 # we can discard the lower point
            else:  # move left
                right = mid 
            
        return left    