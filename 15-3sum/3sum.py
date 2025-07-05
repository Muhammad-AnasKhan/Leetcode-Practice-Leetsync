class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # edge cases

        # sorting
        nums.sort()
        result = []

        for i in range(len(nums)-2):
            j = i + 1
            k = len(nums) - 1

            # avoid duplicate triplets
            if i > 0  and nums[i] == nums[i-1]: continue 

            while j<k:
                threeSum = nums[i] + nums[j] + nums[k] 
                if threeSum== 0:
                    result.append([nums[i], nums[j], nums[k]])
                    while j < k and nums[j] == nums[j+1]:
                        j = j+ 1
                    while j < k and nums[k] == nums[k-1]:
                        k = k-1

                    j = j + 1
                    k = k-1
                elif threeSum > 0:
                    k = k-1
                elif threeSum < 0:
                    j = j + 1

        return result