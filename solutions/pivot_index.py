class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        sum1 = sum2 = 0
        for i in range(0,len(nums)):
            if(sum1 * 2 == total - nums[i]):
                return i
            else: 
                sum1 += nums[i]
        return -1