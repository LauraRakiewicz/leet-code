import numpy as np

class Solution(object):
    def twoSum(self, nums, target):
        np.sort(nums)
        i = 0 
        j = 0
        for i in range(0,len(nums)):
            j = i + 1
            while(j < len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i, j]
                j += 1    
