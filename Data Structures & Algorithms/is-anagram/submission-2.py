class Solution:
    def countChar(self,s):
        count = {}
        for i in s:
            if i not in count: count[i] = 1
            else: count[i]+=1
        return count
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count1 = self.countChar(s)
        count2 = self.countChar(t)
        for k in count1:
            if(count1.get(k) != count2.get(k)):
                return False
        return True