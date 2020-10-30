# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/10/30 22:17
# file: 76_最小覆盖子串.py
# IDE: PyCharm

# 题目描述
# 给你一个字符串 S、一个字符串 T 。请你设计一种算法，可以在 O(n) 的时间复杂度内，从字符串 S 里面找出：
# 包含 T 所有字符的最小子串。

# 示例：
#
# 输入：S = "ADOBECODEBANC", T = "ABC"
# 输出："BANC"
#  
#
# 提示：
#
# 如果 S 中不存这样的子串，则返回空字符串 ""。
# 如果 S 中存在这样的子串，我们保证它是唯一的答案。

# 解法一： 滑动窗口 （双指针）
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        start = left = right = 0
        minLen = float("inf")

        from collections import defaultdict
        # 初始化两个计数器
        needs = defaultdict(int)
        window = defaultdict(int)

        # t:"ABC" ->  needs: {"A": 1, "B": 1, "c": 1}
        for c in t:
            needs[c] += 1

        # 记录window中有多少字符符合要求
        match = 0

        while right < len(s):
            s1 = s[right]
            if s1 in needs:
                # 如果right在t中，则加入window中
                window[s1] += 1
                if window[s1] == needs[s1]:
                    # 字符s1 出现次数符合要求了
                    match += 1
            right += 1

            # window中的字符已经符合needs的要求了
            while match == len(needs):
                # 更新最小子串结果
                if right - left < minLen:
                    start = left
                    minLen = right - left

                s2 = s[left]
                if s2 in needs:
                    # 移出window
                    window[s2] -= 1
                    if window[s2] < needs[s2]:
                        # s2已经不符合要求了
                        match -= 1
                left += 1

        return "" if minLen == float("inf") else s[start:start+minLen]

if __name__ == '__main__':
    s = "ADOBECODEBANC"
    t = "ABC"

    solution = Solution()
    r = solution.minWindow(s, t)
    print(r)