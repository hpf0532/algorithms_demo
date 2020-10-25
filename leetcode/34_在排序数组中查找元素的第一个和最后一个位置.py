# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/10/24 14:19
# file: 34_在排序数组中查找元素的第一个和最后一个位置.py
# IDE: PyCharm

# 题目描述
# 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。
#
# 你的算法时间复杂度必须是 O(log n) 级别。
#
# 如果数组中不存在目标值，返回 [-1, -1]。
#
# 示例 1:
#
# 输入: nums = [5,7,7,8,8,10], target = 8
# 输出: [3,4]
# 示例 2:
#
# 输入: nums = [5,7,7,8,8,10], target = 6
# 输出: [-1,-1]

# 解法一： 二分查找法
from typing import List
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        if size == 0:
            return [-1, -1]

        first_position = self.__find_first_position(nums, size, target)
        if first_position == -1:
            return [-1, -1]
        last_position = self.__find_last_position(nums, size, target)
        return [first_position, last_position]

    def __find_first_position(self, nums, size, target):
        left = 0
        right = size

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                right = mid
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        # 判断越界情况，如果target比nums所有数字都大，nums[size]会越界，在此判断
        if left == size:
            return -1
        return left if nums[left] == target else -1

    def __find_last_position(self, nums, size, target):
        left = 0
        right = size

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid
            else:
                left = mid + 1
        # target比nums中所有数都小，left - 1会越界（-1）, 因此需要判断越界
        # if left == 0:
        #     return -1
        # return left - 1 if nums[left-1] == target else -1
        return left - 1

if __name__ == '__main__':
    n = [1]
    t = 1
    s = Solution()
    r = s.searchRange(n, t)
    print(r)

