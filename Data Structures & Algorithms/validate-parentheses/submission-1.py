class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        validPairs = { ")" : "(", "]" : "[", "}" : "{" }
        for i in s:
            if i in validPairs:
                if stack and stack[-1] == validPairs[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        if not stack:
            return True
        else:
            return False