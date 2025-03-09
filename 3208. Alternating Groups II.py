class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        leng = len(colors)
        if leng < k:
            return 0
        colors = colors+colors[:k-1]
        i = 0
        res = 0
        while i < leng:
            for j in range(i+1, len(colors)):
                if colors[j] == colors[j-1]:
                    i = j
                    break
                else:
                    if j-i == k-1:
                        res += 1
                        i += 1
                if j-i>k-1:
                    i += 1
        return res