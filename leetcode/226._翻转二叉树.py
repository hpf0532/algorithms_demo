# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/12/14 17:21
# file: 226._翻转二叉树.py
# IDE: PyCharm

# 题目描述：
'''

翻转一棵二叉树。

示例：

输入：

     4
   /   \
  2     7
 / \   / \
1   3 6   9
输出：

     4
   /   \
  7     2
 / \   / \
9   6 3   1
备注:
这个问题是受到 Max Howell 的 原问题 启发的 ：

谷歌：我们90％的工程师使用您编写的软件(Homebrew)，但是您却无法在面试时在白板上写出翻转二叉树这道题，这太糟糕了。
'''


# 解法一: 二叉树前序遍历
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        self.left, self.right = self.right, self.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root


# 解法二: 后序遍历
class Solution2:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left
        return root


# 解法三： 迭代
class Solution3:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root

        queue = [root]
        while queue:
            temp = queue.pop(0)
            temp.left, temp.right = temp.right, temp.left
            if temp.left:
                queue.append(temp.left)

            if temp.right:
                queue.append(temp.right)

        return root
