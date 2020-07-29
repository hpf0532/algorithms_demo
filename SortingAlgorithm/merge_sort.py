# -*- coding:utf-8 -*-
# author: hpf
# create time: 2020/7/29 17:52
# file: merge_sort.py
# IDE: PyCharm

# 归并排序是采用分治法的一个非常典型的应用。归并排序的思想就是先递归分解数组，再合并数组。

# 将数组分解最小之后，然后合并两个有序数组，基本思路是比较两个数组的最前面的数，谁小就先取谁，
# 取了后相应的指针就往后移一位。然后再比较，直至一个数组为空，最后把另一个数组的剩余部分复制过来即可。


def merge_sort(alist):
    n = len(alist)
    if n <= 1:
        return alist
    # 二分分解
    mid = n // 2

    # left 采用归并排序后形成的有序的新的列表
    left = merge_sort(alist[:mid])
    # right 采用归并排序后形成的有序的新的列表
    right = merge_sort(alist[mid:])

    # 将两个有序的子序列合并为一个新的整体
    # merge(left, right)
    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left) and right_pointer < len(right):
        if left[left_pointer] < right[right_pointer]:
            result.append(left[left_pointer])
            left_pointer += 1
        else:
            result.append(right[right_pointer])
            right_pointer += 1

    result += left[left_pointer:]
    result += right[right_pointer:]

    return result

if __name__ == '__main__':
    li = [34, 2, 13, 76, 54, 22, 90, 46, 13]
    print(li)
    sort_li = merge_sort(li)
    print(sort_li)


# 时间复杂度
# 最优时间复杂度：O(nlogn)
# 最坏时间复杂度：O(nlogn)
# 稳定性：稳定