class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # seen = {}
        # for num in nums:
        #     if num in seen and seen[num] >= 1:
        #         return True
        #     seen[num] = seen.get(num, 0) + 1
        # return False

        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num) 
        return False

        # return not len(set(nums)) == len(nums)