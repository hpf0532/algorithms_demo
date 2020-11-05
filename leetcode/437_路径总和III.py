# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/11/5 16:09
# file: 437_路径总和III.py
# IDE: PyCharm

# 题目描述
# 给定一个二叉树，它的每个结点都存放着一个整数值。
#
# 找出路径和等于给定数值的路径总数。
#
# 路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。
#
# 二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。
#
# 示例：
#
# root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#       10
#      /  \
#     5   -3
#    / \    \
#   3   2   11
#  / \   \
# 3  -2   1
#
# 返回 3。和等于 8 的路径有:
#
# 1.  5 -> 3
# 2.  5 -> 2 -> 1
# 3.  -3 -> 11


# 解法一： 两层递归

# 思路： 每个node都要计算以它作为起点往下是否有path --> 这是一层递归
# 在考虑当前点为起点往下有没有path的时候，它的path可以往左也可以往右，于是要综合考虑 --> 这是另一层递归

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        return self.dfs(root, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
        pass

    def dfs(self, root, path):
        # 考虑以当前节点为根，向下是否有可用path
        if not root:
            return 0
        path -= root.val
        return (1 if path == 0 else 0) + self.dfs(root.left, path) + self.dfs(root.right, path)
