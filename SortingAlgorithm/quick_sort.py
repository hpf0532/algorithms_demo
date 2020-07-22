# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/7/22 18:42
# file: quick_sort.py
# IDE: PyCharm

def quick_sort(alist, start, end):

    # 递归的退出条件
    if start >= end:
        return
    # n = len(alist)
    # low为序列左边的由左向右移动的游标
    low = start

    # high为序列右边的由右向左移动的游标
    high = end

    # 设定起始元素为要寻找位置的基准元素
    mid = alist[low]


    while low < high:
        # 如果low与high未重合，high指向的元素不比基准元素小，则high向左移动
        while low < high and alist[high] > mid:
            high -= 1
        # 将high指向的元素放到low的位置上
        alist[low] = alist[high]

        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] < mid:
            low += 1
        # 将low指向的元素放到high的位置上
        alist[high] = alist[low]


    # 退出循环后，low与high重合，此时所指位置为基准元素的正确位置
    # 将基准元素放到该位置
    alist[low] = mid

    # 对基准元素左边的子序列进行快速排序
    quick_sort(alist, start, low-1)
    # 对基准元素右边的子序列进行快速排序
    quick_sort(alist, low+1, end)


if __name__ == '__main__':
    li = [34, 2, 13, 76, 54, 22, 90, 46, 13]
    print(li)
    quick_sort(li, 0, len(li)-1)
    print(li)


# 时间复杂度
# 最优时间复杂度：O(nlogn)
# 最坏时间复杂度：O(n2)
# 稳定性：不稳定