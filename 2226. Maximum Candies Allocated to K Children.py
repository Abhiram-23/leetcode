class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        tot = sum(candies)
        if tot < k:
            return 0
        candies = sorted(candies)
        dic = {}
        for i in candies:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        maxi = 0
        val = list(dic.keys())
        # print(val)
        i = 1
        j = max(val)+1
        while i<=j:
            cur = (i+j)//2
            # print(i,j,cur)
            sums = 0
            for l in range(len(val)):
                # print(cur,i,j,val[j])
                sums += (val[l]//cur)*(dic[val[l]])
            # print(sums,k,cur)
            if sums >= k:
                maxi = max(maxi,cur)
                i = cur+1
            else:
                j = cur-1
            # print(maxi)
        return maxi