# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/10/23 9:49
# file: 752_打开转盘锁.py
# IDE: PyCharm

# 题目描述

# 你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为  '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。
#
# 锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。
#
# 列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。
#
# 字符串 target 代表可以解锁的数字，你需要给出最小的旋转次数，如果无论如何不能解锁，返回 -1。

# 示例 1:
#
# 输入：deadends = ["0201","0101","0102","1212","2002"], target = "0202"
# 输出：6
# 解释：
# 可能的移动序列为 "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202"。
# 注意 "0000" -> "0001" -> "0002" -> "0102" -> "0202" 这样的序列是不能解锁的，
# 因为当拨动到 "0102" 时这个锁就会被锁定。

# 示例 2:
#
# 输入: deadends = ["8888"], target = "0009"
# 输出：1
# 解释：
# 把最后一位反向旋转一次即可 "0000" -> "0009"。
# 示例 3:
#
# 输入: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
# 输出：-1
# 解释：
# 无法旋转到目标数字且不被锁定。
# 示例 4:
#
# 输入: deadends = ["0000"], target = "8888"
# 输出：-1
#  
#
# 提示：
#
# 死亡列表 deadends 的长度范围为 [1, 500]。
# 目标数字 target 不会在 deadends 之中。
# 每个 deadends 和 target 中的字符串的数字会在 10,000 个可能的情况 '0000' 到 '9999' 中产生。

from typing import List

# 解法一： BFS
class Solution1:
    def openLock(self, deadends: List[str], target: str) -> int:
        def plusone(s:str, j:int) -> str:
            ch = list(s)
            if ch[j] == '9':
                ch[j] = '0'
            else:
                ch[j] = str(int(ch[j]) + 1)
            return "".join(ch)

        def minusone(s:str, j:int) -> str:
            ch = list(s)
            if ch[j] == '0':
                ch[j] = '9'
            else:
                ch[j] = str(int(ch[j]) - 1)
            return "".join(ch)

        # 记录需要跳过的死亡密码,集合效率高点
        dead = set(deadends)
        # 记录已经穷举过的密码，防止走回头路
        visited = set()
        import queue
        q = queue.Queue()
        # 从起点开始启动广度优先搜索
        step = 0
        q.put("0000")
        visited.add("0000")

        while not q.empty():
            size = q.qsize()
            # 将当前队列中的所有节点向周围扩散
            for _ in range(size):
                cur = q.get()

                if cur in dead:
                    continue
                # 判断是否到达终点
                if cur == target:
                    return step

                # 将一个节点的未遍历相邻节点加入队列
                for j in range(4):
                    up = plusone(cur, j)
                    if up not in visited:
                        q.put(up)
                        visited.add(up)
                    down = minusone(cur, j)
                    if down not in visited:
                        q.put(down)
                        visited.add(down)
            # 增加步数
            step += 1
        # 如果穷举完都没找到目标密码，那就是找不到了
        return -1

# 解法二： 双向BFS
class Solution2:
    def openLock(self, deadends: List[str], target: str) -> int:
        def plusone(s: str, j: int) -> str:
            ch = list(s)
            if ch[j] == '9':
                ch[j] = '0'
            else:
                ch[j] = str(int(ch[j]) + 1)
            return "".join(ch)

        def minusone(s: str, j: int) -> str:
            ch = list(s)
            if ch[j] == '0':
                ch[j] = '9'
            else:
                ch[j] = str(int(ch[j]) - 1)
            return "".join(ch)

        dead = set(deadends)
        visited = set()

        step = 0
        # 用集合不用队列，可以快速判断元素是否存在
        q1 = set()
        q2 = set()
        q1.add("0000")
        q2.add(target)

        while q1 and q2:
            # 用 temp 存储扩散结果
            temp = set()
            if len(q1) > len(q2):
                q1, q2 = q2, q1
            # 将 q1 中的所有节点向周围扩散
            for cur in q1:
                if cur in dead:
                    continue
                if cur in q2:
                    return step
                visited.add(cur)

                # 将一个节点的未遍历相邻节点加入集合
                for j in range(4):
                    up = plusone(cur, j)
                    if up not in visited:
                        temp.add(up)
                    down = minusone(cur, j)
                    if down not in visited:
                        temp.add(down)
            # temp 相当于 q1
            # 这里交换 q1 q2，下一轮 while 就是扩散 q2
            step += 1
            q1 = q2
            q2 = temp
        return -1

if __name__ == '__main__':
    d = ["0201","0101","0102","1212","2002"]
    t = "0202"
    s = Solution2()
    r = s.openLock(d, t)
    print(r)