class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        if len(s1) != len(s2):
            return False
        d1 = ""
        d2 = ""
        for i in range(len(s1)):
            if s1[i]!=s2[i]:
                d1 += s1[i]
                d2 += s2[i]
            if len(d1) >2:
                return False
        if sorted(d1)==sorted(d2):
            return True
        return  False