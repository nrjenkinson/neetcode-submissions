class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for words in strs:
            count = [0] * 26
            for counts in words:
                count[ord(counts) - ord('a')] += 1
            ans[tuple(count)].append(words)
        return list(ans.values())
    
        