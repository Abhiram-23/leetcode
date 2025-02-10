class Solution:
    def clearDigits(self, s: str) -> str:
        a = []
        for i in s:
            if i.isdigit():
                a.pop(-1)
            else:
                a.append(i)
        return "".join(a)