import numpy as np

class Solution(object):
    def plusOne(self, digits):
        plus_one = True
        carry = 1 
        for i in reversed(range(len(digits))):
            last_value = digits[i] + carry
            if(last_value == 10):
                carry = 1
                digits[i] = 0
            else:
                carry = 0
                digits[i] = last_value
        if(carry == 1):
            digits = [1] + digits 
        return digits     