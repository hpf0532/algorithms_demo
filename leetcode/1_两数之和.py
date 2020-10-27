# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/10/27 22:02
# file: 1_两数之和.py
# IDE: PyCharm

# 题目描述：
# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那两个整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
# 示例:

# 给定 nums = [2, 7, 11, 15], target = 9

# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]

# 解法一： 暴力枚举
# 思路： 枚举数组中的每一个数 x，寻找数组中是否存在 target - x。
# 当我们使用遍历整个数组的方式寻找 target - x 时，需要注意到每一个位于 x 之前的元素都
# 已经和 x 匹配过，因此不需要再进行匹配。而每一个元素不能被使用两次，所以我们只需要在
# x 后面的元素中寻找 target - x。
from typing import List
class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

# 解法二： 哈希表
# 思路： 使用哈希表来检索target - x是否存在，提高效率
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        temp = {}
        for i, num in enumerate(nums):
            if target-num in temp:
                return [temp[target-num], i]
            temp[num] = i
        return []

if __name__ == '__main__':
    nums = [3, 2, 4]
    t = 7
    s = Solution2()
    ret = s.twoSum(nums, t)
    print(ret)