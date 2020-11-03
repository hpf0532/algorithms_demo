# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/11/3 14:35
# file: 438_找到字符串中所有字母异位词.py
# IDE: PyCharm

# 题目描述：
# 给定一个字符串 s 和一个非空字符串 p，找到 s 中所有是 p 的字母异位词的子串，返回这些子串的起始索引。
#
# 字符串只包含小写英文字母，并且字符串 s 和 p 的长度都不超过 20100。
#
# 说明：
#
# 字母异位词指字母相同，但排列不同的字符串。
# 不考虑答案输出的顺序。

# 示例 1:
#
# 输入:
# s: "cbaebabacd" p: "abc"
#
# 输出:
# [0, 6]
#
# 解释:
# 起始索引等于 0 的子串是 "cba", 它是 "abc" 的字母异位词。
# 起始索引等于 6 的子串是 "bac", 它是 "abc" 的字母异位词。

# 示例 2:
#
# 输入:
# s: "abab" p: "ab"
#
# 输出:
# [0, 1, 2]
#
# 解释:
# 起始索引等于 0 的子串是 "ab", 它是 "ab" 的字母异位词。
# 起始索引等于 1 的子串是 "ba", 它是 "ab" 的字母异位词。
# 起始索引等于 2 的子串是 "ab", 它是 "ab" 的字母异位词。


# 解法一： 滑动窗口
from typing import List
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # 使用列表记录答案
        res = []
        left = right = 0
        from collections import defaultdict
        needs = defaultdict(int)
        window = defaultdict(int)

        # p="abc"  => needs: {"a":1, "b":1, "c":1}
        for c in p:
            needs[c] += 1

        match = 0

        while right < len(s):
            c1 = s[right]
            if c1 in needs:
                # 右移窗口
                window[c1] += 1
                # 个数相等则match加1
                if window[c1] == needs[c1]:
                    match += 1
            right += 1

            while match == len(needs):
                # 如果 window 的大小合适，就把起始索引 left 加入结果
                if right - left == len(p):
                    res.append(left)

                # 左移窗口
                c2 = s[left]
                if c2 in needs:
                    window[c2] -= 1
                    if window[c2] < needs[c2]:
                        match -= 1
                left += 1
        return res

if __name__ == '__main__':
    s = "cbaebabacd"
    p = "abc"
    s1 = Solution()
    res = s1.findAnagrams(s, p)
    print(res)
