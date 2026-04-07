# Problem: Longest Substring Without Repeating Characters
# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Difficulty: Medium
# Topic: Sliding Window, String

# Approach:
# Use sliding window with set to maintain unique characters

# Time Complexity: O(n)
# Space Complexity: O(n)

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        res_set = set()
        l = 0
        res = 0

        for i in range(len(s)):
            while s[i] in res_set:
                res_set.remove(s[l])
                l += 1

            res_set.add(s[i])
            res = max(res, i - l + 1)

        return res
