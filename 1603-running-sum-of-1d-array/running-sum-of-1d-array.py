class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # Start form index 1, 
        # update each next value adding previous value
        # nums[i] + nums[i-1]
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i-1]
        return nums