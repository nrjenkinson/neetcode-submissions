class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}

        for i, j in enumerate(nums):
            diff = target - j
            if diff in temp:
                return [temp[diff], i]
            temp[j] = i
