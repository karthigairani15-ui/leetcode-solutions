# Problem: Zigzag Conversion
# Link: https://leetcode.com/problems/zigzag-conversion/
# Difficulty: Medium
# Topic: String

# Approach:
# Traverse row by row using pattern gap (2 * (numRows - 1)).
# For middle rows, add diagonal elements as well.

# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s

        res = ""

        for r in range(numRows):
            increment = 2 * (numRows - 1)

            for i in range(r, len(s), increment):
                res += s[i]

                # For middle rows, add diagonal character
                if (r > 0 and r < numRows - 1 and 
                    i + increment - 2*r < len(s)):
                    
                    res += s[i + increment - 2*r]

        return res
