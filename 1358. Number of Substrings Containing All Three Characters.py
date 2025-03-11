class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        dic = {"a":[],"b":[],"c":[]}
        for i in range(len(s)):
            dic[s[i]].append(i)
        k = 0
        op = 0
        if len(dic["a"]) == 0:
            return 0
        elif len(dic["b"]) == 0:
            return 0
        elif len(dic["c"]) == 0:
            return 0
        a = dic["a"][0]
        b = dic["b"][0]
        c = dic["c"][0]
        while k < len(s):  
            maxi = max(a,b,c)
            op += len(s)-maxi
            if a == k:
                dic["a"].pop(0)
                if len(dic["a"]) == 0:
                    break
                a = dic["a"][0]
            elif b == k:
                b = dic["b"].pop(0)
                if len(dic["b"]) == 0:
                    break
                b = dic["b"][0]

            else:
                c = dic["c"].pop(0)
                if len(dic["c"]) == 0:
                    break
                c = dic["c"][0]
            k += 1
        return op