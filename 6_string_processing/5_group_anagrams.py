from pip._vendor.typing_extensions import List


class Solution65:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_map = {}

        for s in strs:
            key = ''.join(sorted(s))
            result_map[key] = result_map.get(key, []) + [s]

        return list(result_map.values())


s = Solution65()
# [["bat"],["nat","tan"],["ate","eat","tea"]]
strs1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(s.groupAnagrams(strs1))
# [[""]]
strs2 = [""]
print(s.groupAnagrams(strs2))
# [["a"]]
strs3 = ["a"]
print(s.groupAnagrams(strs3))
