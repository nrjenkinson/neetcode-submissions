class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        self.nums = nums
        s = set()
        count = 0
        for i in nums:
            s.add(i)
            count += 1
            if count != len(s):
                return True
        return False