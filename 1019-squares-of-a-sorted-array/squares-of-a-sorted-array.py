class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for n in range(len(nums)):
            nums[n] = nums[n] ** 2
        return sorted(nums)