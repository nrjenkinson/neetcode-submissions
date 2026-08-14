class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(filter(str.isalnum, s.lower()))
        length = len(s)

        if length == 0:
            return True

        if length%2 != 0:
            center = length // 2
            i = center
            j = center
        else:
            i = length // 2 - 1
            j = length // 2
        while i >= 0 and j < length:
            if s[i] != s[j]:
                return False
            i -= 1
            j += 1
        return True