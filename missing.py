from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        total = n * (n + 1) // 2
        return total - sum(nums)


obj = Solution()

print(obj.missingNumber([3,0,1]))   # 2
print(obj.missingNumber([0,1]))     # 2