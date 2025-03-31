class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        org = {}
        for i in s:
            if i in org:
                org[i] += 1
            else:
                org[i] = 1
        new = {}
        res = []
        co = 0
        for i in range(len(s)):
            co += 1
            if s[i] in new:
                new[s[i]][0] += 1
            else:
                new[s[i]] = [1,org[s[i]]]
            org[s[i]] -= 1
            if new[s[i]][0] == new[s[i]][1]:
                del new[s[i]]
            if org[s[i]] == 0 and len(new)==0:
                res.append(co)
                co = 0
        if co:
            res.append(co)
        return res