# -*- coding:utf-8 -*-
# author: hpf
# create time: 2021/01/18 20:35
# file: 114_二叉树展开为链表.py
# IDE: PyCharm

# 题目描述
'''
给定一个二叉树，原地将它展开为一个单链表。

例如，给定二叉树

    1
   / \
  2   5
 / \   \
3   4   6
将其展开为：

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
'''

# 解法一: 递归，后序遍历
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        # 后序遍历，此时左右子树已被拉平
        left = root.left
        right = root.right

        # 将右子树变为左子树
        root.left = None
        root.right = left

        # 将右子树接到当前右子树后面
        p = root
        while p.right:
            p = p.right

        p.right = right