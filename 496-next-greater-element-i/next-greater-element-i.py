class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
       
        next_greater = {}
        stack = []

        # Find next greater elements for all elements in nums2
        for num in nums2:
            while stack and stack[-1] < num:
                next_greater[stack.pop()] = num
            stack.append(num)

        # Remaining elements in stack have no next greater element
        while stack:
            next_greater[stack.pop()] = -1

        # Get results for nums1 using precomputed dictionary
        return [next_greater[num] for num in nums1]
