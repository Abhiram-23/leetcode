class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        dic = {}
        dic2 = {}
        op = []
        for i in queries:
            a,b = i
            if a not in dic:
                dic[a] = b
            elif a in dic:
                c = dic[a]
                if dic2[c] == 1:
                    del dic2[c]
                else:
                    dic2[c] -= 1
                dic[a] = b
            if b not in dic2:
                dic2[b] = 1
            else:
                dic2[b] += 1
            op.append(len(dic2))
        return op