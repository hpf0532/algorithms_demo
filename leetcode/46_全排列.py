# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/10/19 9:30
# file: 46_全排列.py
# IDE: PyCharm

# 题目描述
# 示例:

# 输入: [1,2,3]
# 输出:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]

# 回溯算法框架
'''
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return

    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
'''

from typing import List
# 解法一
class Solution1:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 结果集
        res = []
        def dfs(path, nums):
            # 如果路径长度等于数组长度，说明排列成立，添加到结果集中
            if len(path) == len(nums):
                res.append(path[:])
                return

            # 迭代选择列表
            for i in nums:
                # 如果元素在path列表中，跳过
                if i in path:
                    continue
                # 添加到path列表中，继续递归
                path.append(i)
                dfs(path, nums)
                # 状态复位，回溯
                path.pop()

        dfs([], nums)
        return res

# 解法二
class Solution2:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, size, depth, path, used, res):
            if depth == size:
                res.append(path[:])
                return

            for i in range(size):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])

                    dfs(nums, size, depth + 1, path, used, res)

                    used[i] = False
                    path.pop()

        size = len(nums)
        if len(nums) == 0:
            return []

        used = [False for _ in range(size)]
        res = []
        dfs(nums, size, 0, [], used, res)
        return res

# 解法三：
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(nums, tmp):
            if not nums:
                res.append(tmp)
                return
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res



if __name__ == '__main__':
    n = [1,2,3,4]
    s = Solution2()
    ret = s.permute(n)
    print(ret)