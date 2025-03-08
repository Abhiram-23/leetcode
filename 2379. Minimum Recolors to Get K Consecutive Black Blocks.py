class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        op = 101
        i = 0
        co = 0
        for j in range(0,len(blocks)):
            if j < k:
                if blocks[j] == "W":
                    co += 1
                if j == k-1:
                    op = co
            if j >=k:
                if blocks[i] == "W":
                    co -= 1
                i += 1
                if blocks[j] == "W":
                    co += 1
                op = min(op,co)
            if op == 0:
                break
        return op