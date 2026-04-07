# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
class Solution(object):
    def twoSum(self, nums, target):
        d = {}
        
        for i in range(len(nums)):
            value = nums[i]
            diff = target - value
            
            if diff in d:
                return [d[diff], i]
            
            d[value] = i
          
