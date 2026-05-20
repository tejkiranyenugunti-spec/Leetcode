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

#LC 49. Group Anagrams
# I used dictionary, I grouped the words which have the same letters,  each word is sorted  and used it as a kjey in the dictionary, then I added the word to the list of the key,  if the sorted word is same  as another word they will be added to the same zone group, then i returned the values of the dictionary. 
