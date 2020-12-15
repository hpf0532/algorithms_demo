# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/12/15 11:07
# file: 116_填充每个节点的下一个右侧节点指针.py
# IDE: PyCharm

# 题目描述:
'''
给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

 

进阶：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
 
输入：root = [1,2,3,4,5,6,7]
输出：[1,#,2,3,#,4,5,6,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。
 

提示：

树中节点的数量少于 4096
-1000 <= node.val <= 1000

'''


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
# 解法一: 递归
class Solution1:
    def connect(self, root: 'Node') -> 'Node':
        def dfs(node1, node2):
            if not node1 or not node2:
                return

            # 前序遍历，设置连接
            node1.next = node2

            # 连接同父节点
            dfs(node1.left, node1.right)
            dfs(node2.left, node2.right)
            # 连接跨父节点
            dfs(node1.right, node2.left)

        if not root:
            return root

        dfs(root.left, root.right)
        return root


# 解法二: 递归
class Solution2:
    def connect(self, root: 'Node') -> 'Node':
        def dfs(root):
            if not root:
                return root

            left = root.left
            right = root.right

            while left:
                left.next = right
                left = left.right
                right = right.left


            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return root