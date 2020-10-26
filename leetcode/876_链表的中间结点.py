# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/10/26 23:53
# file: 876_链表的中间结点.py
# IDE: PyCharm

# 题目描述：
# 给定一个头结点为 head 的非空单链表，返回链表的中间结点。
#
# 如果有两个中间结点，则返回第二个中间结点。
#
#  
#
# 示例 1：
#
# 输入：[1,2,3,4,5]
# 输出：此列表中的结点 3 (序列化形式：[3,4,5])
# 返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
# 注意，我们返回了一个 ListNode 类型的对象 ans，这样：
# ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
# 示例 2：
#
# 输入：[1,2,3,4,5,6]
# 输出：此列表中的结点 4 (序列化形式：[4,5,6])
# 由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
#  
#
# 提示：
#
# 给定链表的结点数介于 1 和 100 之间。


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# 解法一：数组
# 思路，将链表中所有节点依次添加进有序列表中，并返回中间索引的节点即可
# 时间复杂度：O(N) 空间复杂度：O(N)
class Solution1:
    def middleNode(self, head: ListNode) -> ListNode:
        A = [head]
        # 列表最后一个节点next不为空
        while A[-1].next:
            A.append(A[-1].next)
        # 返回链表中点
        return A[len(A) // 2]

# 解法二：单指针
# 思路：通过两次循环，第一次遍历链表拿到长度，然后将长度与2整除，再遍历找到该节点并返回
# 时间复杂度：O(N) 空间复杂度：O(1)
class Solution2:
    def middleNode(self, head: ListNode) -> ListNode:
        count, cur = 0, head
        # 第一次循环拿到链表长度
        while cur:
            count += 1
            cur = cur.next

        k, cur = 0, head
        # 找到中间位置，拿到节点
        while k < count // 2:
            k += 1
            cur = cur.next
        return cur

# 解法三：双指针（快慢指针）
# 思路：慢指针每次走一步，快指针每次走两步，这样快指针走到链表尾部时，慢指针刚好在中间位置
# 时间复杂度：O(N) 空间复杂度：O(1)
class Solution3:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
