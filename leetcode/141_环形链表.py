# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/10/25 23:18
# file: 141_环形链表.py
# IDE: PyCharm


# 题目描述
# 给定一个链表，判断链表中是否有环。
#
# 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
#
# 如果链表中存在环，则返回 true 。 否则，返回 false 。
#
# 进阶：
#
# 你能用 O(1)（即，常量）内存解决此问题吗？

# 提示：
#
# 链表中节点的数目范围是 [0, 104]
# -105 <= Node.val <= 105
# pos 为 -1 或者链表中的一个 有效索引 。

# 解法一： 哈希表
# 通过遍历所有节点，判断当前是否在哈希表中出现过，如果出现过则说明有环，否则没有环路

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()

        while head:
            # 节点重复，有环
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

# 解法二： 快慢指针
class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next

        return True

# 解法三：快慢指针2
class Solution3:
    def hasCycle(self, head: ListNode) -> bool:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False