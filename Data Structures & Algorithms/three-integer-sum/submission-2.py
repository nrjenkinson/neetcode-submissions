class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        trip = []
        nums.sort()

        for i, k in enumerate(nums):
            if k > 0:
                break
            if i > 0 and k == nums[i-1]:
                continue
            l, r = i+1, len(nums) - 1
            while l < r:
                sums = k + nums[l] + nums[r]
                if sums > 0:
                    r -= 1
                elif sums < 0:
                    l += 1
                else:
                    trip.append([k, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return trip
         