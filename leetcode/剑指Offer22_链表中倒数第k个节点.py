# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/10/27 13:00
# file: 剑指Offer22_链表中倒数第k个节点.py
# IDE: PyCharm

# 题目描述
# 输入一个链表，输出该链表中倒数第k个节点。为了符合大多数人的习惯，本题从1开始计数，
# 即链表的尾节点是倒数第1个节点。例如，一个链表有6个节点，从头节点开始，
# 它们的值依次是1、2、3、4、5、6。这个链表的倒数第3个节点是值为4的节点。

# 示例：
# 给定一个链表: 1->2->3->4->5, 和 k = 2.
# 返回链表 4->5.

# 解法一： 双指针
# 思路： 让快指针先走 k 步，然后快慢指针开始同速前进。这样当快指针走到链表末尾 null 时，
# 慢指针所在的位置就是倒数第 k 个链表节点（为了简化，假设 k 不会超过链表长度）
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        slow = fast = head

        # while k > 0:
        #     fast = fast.next
        #     k -= 1

        for _ in range(k):
            fast = fast.next

        while fast:
            fast, slow = fast.next, slow.next

        return slow

