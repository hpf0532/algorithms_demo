# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/11/10 15:19
# file: 206_反转链表.py
# IDE: PyCharm

# 题目描述
# 反转一个单链表。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL
# 输出: 5->4->3->2->1->NULL
# 进阶:
# 你可以迭代或递归地反转链表。你能否用两种方法解决这道题？

# 解法一： 双指针一
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        cur = None
        pre = head
        while pre:
            t = pre.next
            pre.next = cur
            cur = pre
            pre = t
        return cur

# 解法二:  递归
class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head


# 解法三： 双指针二
class Solution3:
    def reverseList(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        cur = head
        while head:
            t = head.next.next
            head.next.next = cur
            cur = head.next
            head.next = t
        return cur