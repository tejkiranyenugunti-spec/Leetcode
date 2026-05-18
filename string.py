class Solution:
    def lengthOfLongestSubstring(self, s: str):

        seen = set()
        left = 0
        longest = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            longest = max(longest, right - left + 1)

        return longest


obj = Solution()

print(obj.lengthOfLongestSubstring("abcabcbb"))  
print(obj.lengthOfLongestSubstring("bbbbb"))     
print(obj.lengthOfLongestSubstring("pwwkew"))    

# 3. Longest Substring Without Repeating Characters - LC3
#I used a set to store the characters in the current window. I used two pointers, left and right, to represent the current window. After checking and moving, I updated the length accordingly.
