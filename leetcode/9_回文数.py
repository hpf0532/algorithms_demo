# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/11/23 16:51
# file: 9_回文数.py
# IDE: PyCharm

# 题目描述：
# 判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

# 示例 1:

# 输入: 121
# 输出: true
# 示例 2:

# 输入: -121
# 输出: false
# 解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
# 示例 3:

# 输入: 10
# 输出: false
# 解释: 从右向左读, 为 01 。因此它不是一个回文数。
# 进阶:

# 你能不将整数转为字符串来解决这个问题吗？

# 解法一： 转为字符串，双指针法
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

# 解法二:
class Solution2:
    def isPalindrome(self, x: int) -> bool:
        # 特殊情况： x<0 不是回文数
        # 如果最后一位是0，则只有最高位是0才满足回文，只有0符合
        if x < 0 or (x % 10 == 0 and x > 0):
            return False

        reverseNum = 0
        while x > reverseNum:
            reverseNum = reverseNum * 10 + x % 10
            x //= 10

        # 当数字长度为奇数时，我们可以通过，revertedNumber / 10 去除处于中位的数字
        return x == reverseNum or x == reverseNum // 10
