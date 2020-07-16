# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/7/16 21:33
# file: shell_sort.py
# IDE: PyCharm

# 希尔排序(Shell Sort)是插入排序的一种。也称缩小增量排序，是直接插入排序算法的一种更高效的改进版本。
# 希尔排序是非稳定排序算法。该方法因DL．Shell于1959年提出而得名。 希尔排序是把记录按下标的一定增量分组，
# 对每组使用直接插入排序算法排序；随着增量逐渐减少，每组包含的关键词越来越多，当增量减至1时，整个文件恰被分成一组，算法便终止。


def shell_sort(alist):
    n = len(alist)
    # 初始步长
    gap = n // 2

    while gap > 0:
        # 按步长进行插入排序
        for j in range(gap, n):
            i = j
            # 按步长进行插入排序
            while i > 0:
                if alist[i] < alist[i-gap]:
                    alist[i-gap], alist[i] = alist[i], alist[i-gap]
                    i -= gap
                else:
                    break
        # 得到新的步长
        gap //= 2


if __name__ == '__main__':
    li = [34, 2, 13, 76, 54, 22, 90, 46, 13]
    print(li)
    shell_sort(li)
    print(li)


# 时间复杂度
# 最优时间复杂度：根据步长序列的不同而不同
# 最坏时间复杂度：O(n2)
# 稳定想：不稳定