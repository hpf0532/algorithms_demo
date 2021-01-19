# -*- coding:utf-8 -*-
# author: hpf
# create time: 2021/1/19 21:23
# file: 654_最大二叉树.py
# IDE: PyCharm

# 题目描述:
'''
给定一个不含重复元素的整数数组 nums 。一个以此数组直接递归构建的 最大二叉树 定义如下：

二叉树的根是数组 nums 中的最大元素。
左子树是通过数组中 最大值左边部分 递归构造出的最大二叉树。
右子树是通过数组中 最大值右边部分 递归构造出的最大二叉树。
返回有给定数组 nums 构建的 最大二叉树 。


'''

# 解法一: 递归

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if not nums:
            return
        # 找到列表中的最大值
        num = max(nums)
        # 找到最大值索引用于分割左右子序列
        num_i = nums.index(num)
        root = TreeNode(num)

        # 递归调用
        root.left = self.constructMaximumBinaryTree(nums[0:num_i])
        root.right = self.constructMaximumBinaryTree(nums[num_i+1:])
        return root