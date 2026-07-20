class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res1 = 0
        res2 = 0
        res3 = 0
        
        for num in nums:
            res2 |= res1 & num
            res1 ^= num
            res3 = res1 & res2
            res1 ^= res1 & res3
            res2 ^= res2 & res3
        
        return res1
    
    # I solved this problem almost same logic as the previous one  lc 136 but I used 3 variables to keep track of the numbers that have appeared once, twice and thrice. I used bitwise operations to update these variables and finally returned the variable that keeps track of the number that has appeared only once.