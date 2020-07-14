# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/7/14 22:37
# file: select_sort.py
# IDE: PyCharm

# 思路:
# 把一个无序序列看做两部分，前一部分为有序，后一部分为无序
# [ [], 34, 2, 13, 76, 54, 22, 90, 46, 13]
# 从后一部分找出最小值，与第一个元素互换
# 找出次小值，与第二个元素互换，以此类推

def select_sort(alist):
    n = len(alist)
    # 需要进行n-1次选择操作
    for j in range(n-1):
        # 记录最小位置
        min = j
        # 从j+1位置到末尾选择出最小数据
        for i in range(j+1, n):
            if alist[min] > alist[i]:
                min = i

        # 如果选择出的数据不在正确位置，进行交换
        if min != j:
            alist[j], alist[min] = alist[min], alist[j]


if __name__ == '__main__':
    li = [34, 2, 13, 76, 54, 22, 90, 46, 13]
    print(li)
    select_sort(li)
    print(li)


# 时间复杂度:
# 最优时间复杂度：O(n2)
# 最坏时间复杂度：O(n2)
# 稳定性：不稳定（考虑升序每次选择最大的情况）