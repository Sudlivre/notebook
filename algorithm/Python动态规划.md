# Python动态规划

Python在递归中没有像别的语言对递归进行优化，所以他的每一次调用都会基于上一次的调用进行，并且他设置了最大的递归数量防止递归外溢

通过动态规划可以对程序进行优化



#### 例：计算n的阶乘

```python
def factorial1(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    return n * factorial1(n - 1)
 

def factorial2(n: int, m=1) -> int:
    if n == 0 or n == 1:
        return m
    return factorial2(n - 1, n * m)
```



#### 例：小孩爬楼梯

```python
import time
 
 
def steps(n: int) -> int:
    if n < 0:
        return 0
    elif n == 0:
        return 1
    return steps(n - 1) + steps(n - 2) + steps(n - 3)
 
 
for _ in range(5):
    starttime = time.time()
    print('爬楼方式：', steps(25), end=' ')
    endtime = time.time()
    print('计算时间：%.10f' % (endtime-starttime))
```

动态规划

```python
import time
 
 
def steps(n: int, m={}) -> int:
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        try:
            return m[n]
        except:
            m[n] = steps(n - 1) + steps(n - 2) + steps(n - 3)
            return m[n]
 

for _ in range(5):
    starttime = time.time()
    print('爬楼方式：', steps(100), end=' ')
    endtime = time.time()
    print('计算时间：%.10f' % (endtime-starttime))
```

**通过字典将计算过的层数对应的爬楼方式储蓄起来，通过空间换取时间上的领先，这样的领先是巨大的，第一种的写法，基本到后面每一层的计算时间都非常的长，以此看出，算法的设计对程序的运行影响是巨大的**



#### 例：计算列表最大嵌套层数

```python
def list_depth(items: list) -> int:
    max_depth = 1 if isinstance(items, list) else 0
    if max_depth:
        for item in items:
            if isinstance(item, list):
                max_depth = max(max_depth, list_depth(item) + 1)
    return max_depth
 
 
mylist = [1, [2, 3, 4, [5]], [5, [7, [9, 10, [9]]]]]
result = list_depth(mylist)
print(f'最大的嵌套层数为：{result}')
```



#### 例：字符消除游戏

```python
def get_max_remove_number(s, ss):
    # do something
    return 0
```

