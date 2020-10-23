# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/10/23 23:38
# file: 704_二分查找.py
# IDE: PyCharm

# 题目描述
# 给定一个 n 个元素有序的（升序）整型数组 nums 和一个目标值 target  ，写一个函数搜索 nums 中的 target，如果目标值存在返回下标，否则返回 -1。
#
#
# 示例 1:
#
# 输入: nums = [-1,0,3,5,9,12], target = 9
# 输出: 4
# 解释: 9 出现在 nums 中并且下标为 4
# 示例 2:
#
# 输入: nums = [-1,0,3,5,9,12], target = 2
# 输出: -1
# 解释: 2 不存在 nums 中因此返回 -1
#  
#
# 提示：
#
# 1. 你可以假设 nums 中的所有元素是不重复的。
# 2. n 将在 [1, 10000]之间。
# 3. nums 的每个元素都将在 [-9999, 9999]之间。

from typing import List

# 二分查找
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        # 相当于两端都闭区间 [left, right]
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            # 找到target
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                # mid已被搜索过，-1
                right = mid - 1
            else:
                # 同上
                left = mid + 1
        return -1


if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12, 25, 36, 54, 98, 234]
    target = 12
    s = Solution()
    r = s.search(nums, target)
    print(r)

