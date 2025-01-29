class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # the idea is to strat with the first elem as current pointer.
        # and compare it with upcoming elements and update the counter. 
        
        # if consective chains breaks, reset the counter
        
        if(len(nums)==0):
            return 0
        nums = sorted(list(set(nums)))
        print(nums)
        current = nums[0]
        count = 1
        max_count = count
        for i in range(1,len(nums)):
            if nums[i] == current + 1 or nums[i] == current:
                count += 1
                current = nums[i]
                max_count = max(max_count, count)
            else:
                max_count = max(max_count, count)
                count = 1
                current = nums[i]

        return max_count


        