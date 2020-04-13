import numpy as np 

class Solution(object):
    def singleNumber(self, nums):
        hash_table = {}
        for i in nums:
            hash_table[i] += 1 

        for i in hash_table:
            hash_table[i] == 1:
                return i 