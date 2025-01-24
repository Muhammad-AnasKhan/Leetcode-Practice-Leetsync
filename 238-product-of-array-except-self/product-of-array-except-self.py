class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = [1] * len(nums)
        
        # left = 1
        # for i in range(len(nums)):
        #     output[i] *= left
        #     left *= nums[i]
        
        # right = 1
        # for i in range(len(nums) - 1, -1, -1):
        #     output[i] *= right
        #     right *= nums[i]
    
        # return output   
    
        # O(n) solution

        # the idea is, value at i will be equal to the 
        # multiple of all the value at 
        # its (<- left ) and its (right ->)

        # so we will keep two arrays for left and write and 
        # then mutiply both to get the answer array
        n = len(nums)
        left_multiples = [1]
        right_multiples = [0] * n

        l = 1
        for i in range(1,n):
            l = l * nums[i - 1] # take multiple of all elements at left of i
            left_multiples.append(l)
        
        r = 1
        for i in range(n-1,-1,-1):
            if i == n-1:
                right_multiples[i] = r
            else:
                r =  nums[i+1] * r
                right_multiples[i] = r


        return [i*j for i,j in zip(left_multiples,right_multiples)]