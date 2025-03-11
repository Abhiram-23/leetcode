from collections import deque
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rc = 0
        dc = 0
        a = deque([])
        for i in senate:
            a.append(i)
            if i == "R":
                rc += 1
            else:
                dc += 1
        if len(a) == rc:
                return "Radiant"
        elif len(a) == dc:
            return "Dire"
        while True:
            b = a.popleft()
            if b == "D":
                a.remove("R")
                rc -= 1
                a.append("D")
            else:
                a.remove("D")
                dc -= 1
                a.append("R")
            if len(a) == rc:
                return "Radiant"
            elif len(a) == dc:
                return "Dire"