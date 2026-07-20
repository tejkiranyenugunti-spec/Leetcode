class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res = n ^ res
        return res


# I solved this problem by using XOR operation , initially i kept the res as 0 and then i iterated through each number and did XOR operation with numbers and return the res.