class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        left, right = 0, len(s)
        maxLength = 0

        for r in range(right):
            while s[r] in chars:
                chars.remove(s[left])
                left += 1
            chars.add(s[r])
            maxLength = max(maxLength, r - left + 1)
        
        return maxLength

        