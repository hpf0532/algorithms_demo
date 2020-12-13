# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/12/12 18:05
# file: 234_回文链表.py
# IDE: PyCharm

# 题目描述：
'''
请判断一个链表是否为回文链表。

示例 1:
输入: 1->2
输出: false
示例 2:

输入: 1->2->2->1
输出: true
进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 解法一: 将值复制到数组中后用双指针法
class Solution1:
    def isPalindrome(self, head: ListNode) -> bool:
        vals = []
        while head is not None:
            vals.append(head.val)
            head = head.next

        return vals == vals[::-1]


# 解法二: 递归法
class Solution2:
    def isPalindrome(self, head: ListNode) -> bool:
        self.left_node = head

        def traverse(node):
            if node is None:
                return True
            res = traverse(node.next)
            res = res and node.val == self.left_node.val
            self.left_node = self.left_node.next

            return res
        return traverse(head)

# 解法三: 快慢指针法
class Solution3:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None:
            return True

        first_half_end = self.end_of_first_half(head)
        second_half_start = self.reverse_list(first_half_end.next)

        # 判断回文
        result = True
        first_position = head
        second_position = second_half_start
        while result and second_position is not None:
            if first_position.val != second_position.val:
                return False
            first_position = first_position.next
            second_position = second_position.next

        # 还原链表并返回结果
        first_half_end.next = self.reverse_list(second_half_start)
        return result

    # 寻找链表中点
    def end_of_first_half(self, head):
        fast = head
        slow = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

    # 反转链表
    def reverse_list(self, head):
        previous = None
        current = head
        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node
        return previous