# -*- coding:utf-8 -*-

"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_list = []
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] + nums[j] == target and (i, j) != (j, i):
                    index_list = [i, j]
        return index_list


if __name__ == '__main__':
    nums1 = [2, 7, 11, 15]
    target1 = 9
    s = Solution()
    s1 = s.twoSum(nums1, target1)
    print(s1)
