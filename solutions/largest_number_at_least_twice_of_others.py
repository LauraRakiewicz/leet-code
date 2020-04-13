class Solution(object):
	def dominantIndex(self, nums):
	max_value = max(nums)
	if all(x*2 <= max_value for x in nums if(x != max_value)):
		return nums.index(max_value)
	return -1