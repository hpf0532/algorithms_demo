# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/10/26 23:18
# file: 142_环形链表II.py
# IDE: PyCharm

# 题目描述：
# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
#
# 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。
#
# 说明：不允许修改给定的链表。
#
# 进阶：
#
# 你是否可以使用 O(1) 空间解决此题？

# 提示：
#
#  - 链表中节点的数目范围在范围 [0, 104] 内
#  - -105 <= Node.val <= 105
#  - pos 的值为 -1 或者链表中的一个有效索引

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 解法一： 哈希表
class Solution1:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 存储遍历过的节点
        seen = set()

        while head:
            # 如果节点重复，表明出现环路，该节点也是环路起点，返回即可
            if head in seen:
                return head
            seen.add(head)
            head = head.next
        # 没有环路情况
        return None

# 解法二：双指针（快慢指针）
class Solution2:
    def detectCycle(self, head: ListNode) -> ListNode:
        slow = fast = head

        while True:
            if not (fast and fast.next):
                return None
            slow = slow.next
            fast = fast.next.next
            # 双指针第一次相遇，假设slow走了n步，则此时fast走了2n步，相当于多走了一个环的长度n
            if slow == fast:
                break

        # 设相遇点距环的起点的距离为m，那么环的起点距头结点head的距离为k - m，也就是说如果从
        # head前进k - m步就能到达环起点。巧的是，如果从相遇点继续前进k - m步，也恰好到达环起点。
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow
