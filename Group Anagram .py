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


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))

# I used a dictionary to group the anagrams together. I sorted each word to create a key and then added the original word to the list of anagrams corresponding to that key. Finally, I returned the values of the dictionary as a list of lists.