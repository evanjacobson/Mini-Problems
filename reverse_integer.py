# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
#
# https://leetcode.com/problems/reverse-integer/

class Solution:
    def reverse(self, x: int) -> int:
        arr = []
        total = 0
        z = x if x >= 0 else x * -1
        while( z > 0 ):
            arr.append(int(z % 10))
            z = int((z-(z%10)) / 10)
        if(len(arr) == 0):
            return 0
        sarr = [str(i) for i in arr]
        total = int("".join(sarr))
        if x < 0:
            total = total * -1
            
        return total if total >= -2147483648 and total <= 2147483647 else 0
