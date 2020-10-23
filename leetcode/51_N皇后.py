# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/10/20 16:41
# file: 51_N皇后.py
# IDE: PyCharm

# 题目描述:
# n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

# 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
# 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。
#
# 示例：
#
# 输入：4
# 输出：[
#  [".Q..",  // 解法 1
#   "...Q",
#   "Q...",
#   "..Q."],
#
#  ["..Q.",  // 解法 2
#   "Q...",
#   "...Q",
#   ".Q.."]
# ]
# 解释: 4 皇后问题存在两个不同的解法。



from typing import List

# 解法一: 回溯
class Solution1:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        def dfs(r, col, pie, na):
            # 所有行都找完了，每行都放置了一个皇后
            if len(col) == n:
                res.append(col)
            # 下一行，尝试放置到不同位置
            for i in range(n):
                if i not in col and r - i not in pie and r + i not in na:
                    dfs(r + 1, col + [i], pie + [r - i], na + [r + i])

        dfs(0, [], [], [])
        print(res)
        return [["." * i + "Q" + "." * (n-i-1) for i in item] for item in res]


# 解法二:
class Solution2:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n < 1:
            return []
        self.result = []
        self.cols = set()
        self.pie = set()
        self.na = set()
        self.DFS(n, 0, [])
        # return [["." * i + "Q" + "." * (n-i-1) for i in item] for item in self.result]
        return self.get_result(n)

    def get_result(self, n):
        board = []
        for item in self.result:
            for i in item:
                board.append("."*i + "Q" + "."*(n-i-1))
        return [board[i: i+n] for i in range(0, len(board), n)]


    def DFS(self, n, row, cur_state):
        if row == n:
            self.result.append(cur_state)
            return

        for col in range(n):
            if col in self.cols or row + col in self.pie or row - col in self.na:
                continue

            self.cols.add(col)
            self.pie.add(row + col)
            self.na.add(row - col)

            self.DFS(n, row + 1, cur_state + [col])

            self.cols.remove(col)
            self.pie.remove(row + col)
            self.na.remove(row - col)


if __name__ == '__main__':
    s = Solution1()
    r = s.solveNQueens(4)
    print(r)