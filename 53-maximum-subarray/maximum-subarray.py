class Solution:
    def maxSubArray(self, nums: List[int]) -> int:            
        # Cubic solution:
        # 1 loop for i, one for j (sub array), 1 for k(to calculate sub array sum)
        
        # Quadratic solution:
        # 1 loop for i, i for j (subarray), and save the previous subarray sum 

        # linear solution
        # the idea is to go through the array, and ignore the the sub arrays resulting in -ve sum(value)

        maxSubSum = nums[0]
        currentSum = 0

        for i in nums:
            if currentSum < 0:
                currentSum = 0 # reset to 0 if found -ve result, to keep the result contiguos

            currentSum += i
            maxSubSum = max(currentSum, maxSubSum)

        return maxSubSum