class Solution:

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        r = 0
        c = cols - 1

        while r < rows and c >= 0:
            current = matrix[r][c]

            if current == target:
                return True
            elif current > target:
                c -= 1
            else:
                r += 1

        return False
    
    # I solved this problem by using a two-pointer approach. I started from the top-right corner of the matrix and compared the current element with the target. If the current element is equal to the target, I returned True. If the current element is greater than the target, I moved left (decremented the column index). If the current element is less than the target, I moved down (incremented the row index). I continued this process until I either found the target or went out of bounds of the matrix. If I exited the loop without finding the target, I returned False.