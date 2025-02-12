from collections import defaultdict
# from typing import List
class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        # nums = sorted(nums)
        # a = []
        # for i in nums:
        #     b = str(i)
        #     a.append(sum(map(int, str(b))))
        # sorted_x, sorted_y = zip(*sorted(zip(a, nums)))
        # op = -1
        # for i in range(len(a)):
        #     for j in range(i+1,len(a)):
        #         if sorted_x[i] == sorted_x[j]:
        #             op = max(op,sorted_y[i]+sorted_y[j])
        #         elif sorted_x[i] != sorted_x[j]:
        #             break
        # return op
        digit_sum_map = defaultdict(list)

        # Group numbers by their digit sum
        for num in nums:
            digit_sum = sum(map(int, str(num)))
            digit_sum_map[digit_sum].append(num)

        max_sum = -1

        # Find the max sum of any two numbers with the same digit sum
        for num_list in digit_sum_map.values():
            if len(num_list) > 1:
                num_list.sort(reverse=True)  # Sort in descending order
                max_sum = max(max_sum, num_list[0] + num_list[1])

        return max_sum