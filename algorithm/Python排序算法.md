# Python排序算法

#### 顺序查找（Sequence Search）

顺序查找是按照序列原有顺序对数组进行遍历比较查询的基本查找算法。

```python
def seq_search(items, elem):
    """顺序查找"""
    for index, item in enumerate(items):
        if item == elem:
            return index
    return -1
```



#### 二分查找/折半查找（Binary Search）

二分查找是一种效率较高的查找方法。但是，折半查找要求线性表必须采用顺序存储结构，而且表中元素按关键字有序排列。

```python
def bin_search(items, elem):
    """折半查找(二分查找)"""
    start, end = 0, len(items) - 1
    while start <= end:
        mid = (start + end) // 2
        if elem < items[mid]: end = mid - 1 elif elem > items[mid]:
            start = mid + 1
        else:
            return mid
    return -1
```



#### 冒泡排序（Bubble Sort）

冒泡排序是一种计算机科学领域的较简单的排序算法。它重复地走访过要排序的元素列，依次比较两个相邻的元素，如果他们的顺序（如从大到小、首字母从A到Z）错误就把他们交换过来。走访元素的工作是重复地进行直到没有相邻元素需要交换，也就是说该元素已经排序完成。

```python
# 实现排序自定义，避免极端情况，正向逆向都比较一次
def bubble_sort(origin_items, *, comp=lambda x, y: x > y):
    """冒泡排序"""
    items = origin_items[:]
    length = len(items)
    for i in range(1, length):
        swapped = False
        for j in range(0, length - i):
            if comp(items[j], items[j + 1]):
                items[j], items[j + 1] = items[j + 1], items[j]
                swapped = True
        if swapped:
            swapped = False
            for j in range(length - i - 1, i - 1, -1):
                if comp(items[j - 1], items[j]):
                    items[j - 1], items[j] = items[j], items[j - 1]
                    swapped = True
        if not swapped:
            break
    return items
```



#### 归并排序（Merge Sort）

归并排序是建立在归并操作上的一种有效的排序算法,该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为二路归并。

```python
def merge(list1, list2, comp=lambda x, y: x <= y):
    """"有序合并(将两个有序的列表合并成一个新的有序的列表)"""
    list3 = []
    index1, index2 = 0, 0
    while index1 < len(list1) and index2 < len(list2):
        if comp(list1[index1], list2[index2]):
            list3.append(list1[index1])
            index1 += 1
        else:
            list3.append(list2[index2])
            index2 += 1
    list3 += list1[index1:]
    list3 += list2[index2:]
    return list3
 
 
def merge_sort(origin_items, comp=lambda x, y: x <= y):
    """归并排序"""
    if len(origin_items) < 2:
        return origin_items[:]
    mid = len(origin_items) // 2
    left = merge_sort(origin_items[:mid], comp)
    right = merge_sort(origin_items[mid:], comp)
    return merge(left, right, comp)
```

