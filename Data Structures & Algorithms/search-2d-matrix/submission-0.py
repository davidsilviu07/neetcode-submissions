class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        randuri, coloane = len(matrix), len(matrix[0])
        l, r = 0, randuri * coloane - 1
        while l <= r:
            m = (l + r) // 2
            val = matrix[m // coloane][m % coloane]
            if val == target:
                return True
            elif val < target:
                l = m + 1
            else:
                r = m - 1
        return False