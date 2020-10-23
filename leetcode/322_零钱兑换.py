# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/10/17 21:52
# file: 322_零钱兑换.py
# IDE: PyCharm

# 题目描述

# 给定不同面额的硬币 coins 和一个总金额 amount。
# 编写一个函数来计算可以凑成总金额所需的最少的硬币个数。
# 如果没有任何一种硬币组合能组成总金额，返回 -1。
#
# 你可以认为每种硬币的数量是无限的。

# 示例 1：
#
# 输入：coins = [1, 2, 5], amount = 11
# 输出：3
# 解释：11 = 5 + 5 + 1

# 示例 2：
#
# 输入：coins = [2], amount = 3
# 输出：-1


# 解法一： 暴力递归
from typing import List

def coinChange1(coins: List[int], amount: int) -> int:
    def dp(n):
        # 递归退出条件, 0表示可以找零，<0 则无解
        if n == 0: return 0
        if n < 0: return -1
        # 求最小值，初始化为正无穷
        res = float("INF")
        for coin in coins:
            subproblem = dp(n - coin)
            # 子问题无解，跳过
            if subproblem == -1:
                continue
            # 求子问题最小值
            res = min(res, subproblem + 1)
        # 返回结果
        return res if res != float("INF") else -1

    return dp(amount)

# 解法二: 带备忘录的递归
def coinChange2(coins: List[int], amount: int) -> int:
    # 备忘录
    memo = dict()
    def dp(n):
        # 递归退出条件, 0表示可以找零，<0 则无解
        if n == 0: return 0
        if n < 0: return -1
        # 如果已经计算过，则直接返回
        if n in memo: return memo[n]
        # 求最小值，初始化为正无穷
        res = float("INF")
        for coin in coins:
            subproblem = dp(n - coin)
            # 子问题无解，跳过
            if subproblem == -1:
                continue
            # 求子问题最小值
            res = min(res, subproblem + 1)

        # 存入备忘录
        memo[n] = res if res != float("INF") else -1
        return memo[n]

    return dp(amount)

# 解法三： 动态规划
def coinChange3(coins: List[int], amount: int) -> int:
    # 数组大小为 amount + 1，初始值也为 amount + 1
    dp = [amount+1] * (amount+1)
    # 金额为0时，找零也为0
    dp[0] = 0
    # 外层for 循环在遍历所有状态的所有取值
    for i in range(1, amount+1):
        # 内层for 循环在求所有选择的最小值
        for coin in coins:
            # 子问题无解，跳过
            if i-coin < 0:
                continue
            dp[i] = min(dp[i], dp[i-coin] + 1)

    return dp[amount] if dp[amount] != (amount+1) else -1


if __name__ == '__main__':
    coins = [1, 3, 4]
    amount = 25

    ret = coinChange1(coins, amount)
    print("ret1: {}".format(ret))

    ret = coinChange2(coins, amount)
    print("ret2: {}".format(ret))

    ret = coinChange3(coins, amount)
    print("ret3: {}".format(ret))



