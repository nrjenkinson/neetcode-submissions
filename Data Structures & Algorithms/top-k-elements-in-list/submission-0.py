class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = [[] for i in range(len(nums) + 1)] 
        map = {}
        
        for num in nums:
            map[num] = 1 + map.get(num,0)
        for num,counts in map.items():
            ans[counts].append(num)
        
        res = []
        for i in range(len(ans) -1, 0, -1):
            for num in ans[i]:
                res.append(num)
                if len(res) == k:
                    return res