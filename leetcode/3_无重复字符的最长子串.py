# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/11/4 18:37
# file: 3_无重复字符的最长子串.py
# IDE: PyCharm

# 题目描述
# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

# 示例 1:
#
# 输入: "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
# 示例 2:
#
# 输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
# 示例 3:
#
# 输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
# 请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。

# 解法一： 滑动窗口1
class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 记录最长长度
        res = 0
        left = right = 0
        from collections import defaultdict
        window = defaultdict(int)

        n = len(s)
        while right < n:
            c1 = s[right]
            window[c1] += 1
            right += 1

            # 如果window中出现重复字符,开始移动left缩小窗口
            while window[c1] > 1:
                c2 = s[left]
                window[c2] -= 1
                left += 1

            res = max(res, right - left)
        return res

# 解法二: 滑动窗口2
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        occ = set()
        n = len(s)
        right = res = 0
        for left in range(n):
            while right < n and s[right] not in occ:
                occ.add(s[right])
                right += 1
            if len(occ) > res:
                res = len(occ)
            occ.remove(s[left])
        return res

if __name__ == '__main__':
    s = "pwwkew"
    solu = Solution2()
    ret = solu.lengthOfLongestSubstring(s)
    print(ret)
