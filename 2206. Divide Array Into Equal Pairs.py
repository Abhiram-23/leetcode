class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        dic = {}
        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        for i in list(dic.values()):
            if i%2==1:
                return False
        return True