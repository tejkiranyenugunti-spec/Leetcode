from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ans = {}

        for word in strs:

            key = "".join(sorted(word))

            if key not in ans:
                ans[key] = []

            ans[key].append(word)

        return list(ans.values())


obj = Solution()

print(obj.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

