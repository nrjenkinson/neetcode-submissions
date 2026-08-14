class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = {}
        for string in strs:
            sorted_str = ''.join(sorted(string))
            if sorted_str not in map:
                map[sorted_str] = []
            map[sorted_str].append(string)
        return list(map.values())

    
        