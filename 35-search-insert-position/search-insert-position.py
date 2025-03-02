class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # the idea is to find the index where the target is or should be inserted
        # if the element at i is greater than or equal to the target then return i
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        
        # if no element found, return the length(next index) of the array
        return len(nums)