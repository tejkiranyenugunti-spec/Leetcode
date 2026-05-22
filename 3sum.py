from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        result = []

        for i in range(len(nums)):

      
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:

                total = nums[i] + nums[left] + nums[right]

            
                if total == 0:

                    result.append([nums[i], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    left += 1

               
                else:
                    right -= 1

        return result


obj = Solution()

print(obj.threeSum([-1,0,1,2,-1,-4]))

#I used sorting and the two-pointer approach. to avoid the duplicates, I checked if the current number is the same as the previous one and skipped it.  