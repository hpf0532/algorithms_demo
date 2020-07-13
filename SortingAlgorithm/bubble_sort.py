# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/7/13 21:39
# file: bubble_sort.py
# IDE: PyCharm
def bubble_sort(alist):
    """冒泡排序"""
    n = len(alist)
    #外层循环控制内层循环执行几次
    for j in range(n-1):
        #内层循环从头走到尾
        for i in range(0, n-1-j):
            # 如果前一个大，则交换位置
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


def bubble_sort1(alist):
    n = len(alist)
    for j in range(n-1, 0, -1):
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]


def bubble_sort2(alist):
    """冒泡排序优化"""
    n = len(alist)
    for j in range(n-1):
        count = 0
        for i in range(n-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]
                count += 1

        # 如果一次下来没有发生交换，说明原来就有序，直接返回
        if count == 0:
            return




    # n-1-0 j=0
    # n-1-1 j=1
    # n-1-2 j=2
    # 1     j = n-1

if __name__ == '__main__':
    li = [34, 2, 13, 76, 54, 22, 90, 46, 13]
    print(li)
    bubble_sort2(li)
    print(li)

# 冒泡排序:
# 最优时间复杂度：O(n) （表示遍历一次发现没有任何可以交换的元素，排序结束。）
# 最坏时间复杂度：O(n2)
# 稳定性：稳定