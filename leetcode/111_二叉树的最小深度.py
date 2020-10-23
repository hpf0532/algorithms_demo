# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/10/22 9:38
# file: 111_二叉树的最小深度.py
# IDE: PyCharm

# 题目描述：
# 给定一个二叉树，找出其最小深度。
#
# 最小深度是从根节点到最近叶子节点的最短路径上的节点数量。
#
# 说明: 叶子节点是指没有子节点的节点。
#
# 示例:
#
# 给定二叉树 [3,9,20,null,null,15,7],
#
#     3
#    / \
#   9  20
#     /  \
#    15   7
# 返回它的最小深度  2.

# 解法一： BFS

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0

        from collections import deque
        q = deque()

        # root本身就是一层，depth初始化为1
        q.append(root)
        depth = 1

        while(q):
            size = len(q)
            # 将当前队列中的所有节点向四周扩散
            for _ in range(size):
                node = q.popleft()
                # 判断是否到达终点
                if not node.left and not node.right:
                    return depth
                # 将node的相邻节点加入队列
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            # 这里增加步数
            depth += 1

        return depth

# 解法二： DFS

# 先看使用 DFS（深度优先搜索）的方法，具体做法如下：
#
# 根节点为空，返回 0；
# 如果根节点不为空，需要判断左右子节点：
# 左右子节点都为空，那么返回 1；
# 左右子节点其中一个为空，那么返回不为空子节点的最小深度；
# 左右子节点均不为空，返回其中较小深度的值。



class Solution:
    def minDepth(self, root: TreeNode) -> int:
        # 根节点为空
        if not root:
            return 0
        # 根节点不为空，但不存在左右子节点，返回 1
        if not root.left and not root.right:
            return 1

        depth = 1

        # 返回不为空的右子节点最小深度
        if not root.left:
            depth += self.minDepth(root.right)
        # 不存在右子节点，返回不为空的左子节点最小深度
        elif not root.right:
            depth += self.minDepth(root.left)
        # 左右子节点均不为空，返回较小深度
        else:
            left_depth = self.minDepth(root.left)
            right_depth = self.minDepth(root.right)
            depth += min(left_depth, right_depth)

        return depth