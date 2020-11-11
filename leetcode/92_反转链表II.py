# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/11/11 17:19
# file: 92_反转链表II.py
# IDE: PyCharm

# 题目描述：
# 反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。
#
# 说明:
# 1 ≤ m ≤ n ≤ 链表长度。
#
# 示例:
#
# 输入: 1->2->3->4->5->NULL, m = 2, n = 4
# 输出: 1->4->3->2->5->NULL

# 解法一： 递归
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        def reverseListNode(head, n):
            """
            反转链表前N个节点
            :param head:
            :param n:
            :return:
            """
            if n == 1:
                return head

            last = reverseListNode(head.next, n - 1)
            succeed = head.next.next
            head.next.next = head
            head.next = succeed
            return last

        if m == 1:
            # m等于1，相当于反转前N个节点
            return reverseListNode(head, n)
        head.next = self.reverseBetween(head.next, m - 1, n - 1)
        return head


# 解法二： 双指针，虚假头结点，迭代
class Solution2:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head

        dummy = ListNode(-1)
        dummy.next = head
        # a -> m的前一个节点， d -> n所在节点
        a, d = dummy, dummy
        for _ in range(m - 1):
            a = a.next

        for _ in range(n):
            d = d.next

        # b -> m所在节点， c -> n后面的节点
        b, c = a.next, d.next
        pre = b
        cur = pre.next
        while cur != c:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        a.next = d
        b.next = c
        return dummy.next