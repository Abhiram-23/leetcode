class Solution:
    def coloredCells(self, n: int) -> int:
        op = 1
        for i in range(n):
            op += i*4
        return op