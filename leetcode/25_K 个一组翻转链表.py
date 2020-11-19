# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/11/19 22:02
# file: 25_K个一组翻转链表.py
# IDE: PyCharm

# 题目描述:
# 给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。
# k 是一个正整数，它的值小于或等于链表的长度。
# 如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

# 示例：

# 给你这个链表：1->2->3->4->5
# 当 k = 2 时，应当返回: 2->1->4->3->5
# 当 k = 3 时，应当返回: 3->2->1->4->5

# 说明：
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

# 解法一: 迭代 + 递归
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, a, b):
        """
        翻转链表[a, b)区间
        :param a:
        :param b:
        :return:
        """
        pre = None
        cur = a
        while cur != b:
            cur.next, pre, cur = pre, cur, cur.next
        return pre

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return
        a = b = head
        # 获取从head开始k个元素的子链表
        for _ in range(k):
            if not b:
                return head
            b = b.next

        # 递归返回新的头节点
        newHead = self.reverse(a, b)
        # 将原来的头节点继续指向后面的递归结果
        a.next = self.reverseKGroup(b, k)
        return newHead