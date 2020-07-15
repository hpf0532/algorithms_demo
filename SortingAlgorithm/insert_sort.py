# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/7/15 21:58
# file: insert_sort.py
# IDE: PyCharm


# 插入排序：
# 思想
# 将序列分为两部分，以此从后面的序列取出一个元素与前一个序列中的元素比较，找到合适的位置插入，直到最后一个元素为止。
# 首先假定序列的第一个元素为有序序列，拿第二个元素与之比较，找到合适位置后，换下一个元素，以此类推

# 与选择排序的区别：
# 插入排序是依次从后序序列中取出元素与前一个序列中的元素比较，找到其位置
# 选择排序则是找到后一个序列中的最小值，插入到前面的序列

def insert_sort(alist):
    n = len(alist)
    for j in range(1, n):
        # j = [1, 2, 3, ... n-1]
        # i 代表内层循环起始值
        i = j
        # 执行从右边无序序列中取出第一个元素，即i位置的元素，然后将其插入到前面的正确位置
        while i > 0:
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]
                i -= 1
            # 优化: 如果没有交换，说明就是最大值
            else:
                break


def insert_sort1(alist):
    n = len(alist)
    # 从第二个位置，即下标为1的元素开始向前插入
    for j in range(1, n):
        # 从第j个元素开始向前比较，如果小于前一个元素，交换位置
        for i in range(j, 0, -1):
            if alist[i] < alist[i-1]:
                alist[i], alist[i-1] = alist[i-1], alist[i]



if __name__ == '__main__':
    li = [34, 2, 13, 76, 54, 22, 90, 46, 13]
    print(li)
    insert_sort1(li)
    print(li)


# 时间复杂度
# 最优时间复杂度：O(n) （升序排列，序列已经处于升序状态）
# 最坏时间复杂度：O(n2)
# 稳定性：稳定