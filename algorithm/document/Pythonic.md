# Pythonic写优雅的Python代码

**《Python之禅》中的几句经典阐释：**

优美胜于丑陋（Python 以编写优美的代码为目标）

明了胜于晦涩（优美的代码应当是明了的，命名规范，风格相似）

简洁胜于复杂（优美的代码应当是简洁的，不要有复杂的内部实现）

复杂胜于凌乱（如果复杂不可避免，那代码间也不能有难懂的关系，要保持接口简洁）

扁平胜于嵌套（优美的代码应当是扁平的，不能有太多的嵌套）

间隔胜于紧凑（优美的代码有适当的间隔，不要奢望一行代码解决问题）

可读性很重要（优美的代码是可读的）

#### 1、变量值交换

这个问题最常见，通常是通过一个临时变量来实现的：

```python
tmp = a
a = b
b = tmp
```

Python中可以直接交换两个变量，即：

```
a, b = b, a
```

#### **2、列表推导式**

列表推导式简洁的实现for循环，可以应用于列表，集合或者字典。

例如我们要求20以内的整除3的数的平方的列表，可以用如下代码实现：

```python
numbers = []
for x in range(20):    
    if x % 3 == 0:        
        numbers.append(x*x)
```

而通过列表推导式一行代码即可实现：

```python
numbers = [x*x for x in range(20) if x % 3 == 0]
```

列表推导式也可以用于集合和字典，将[…]变为{…}即可。集合和字典的实现如下所示：

集合：

```python
numbers = {x * x for x in range(0, 20) if x % 3 == 0}
```

字典：

```python
numbers = {x: x * x for x in range(0, 20) if x % 3 == 0}
```

#### **3、字符串拼接**

这是一个老生常谈的问题，当我们需要将数个字符串拼接的时候，习惯性的使用 “+” 作为连接字符串的手段。

然而，由于像字符串这种不可变对象在内存中生成后无法修改，合并后的字符串会重新开辟出一块内存空间来存储。因此每合并一次就会单独开辟一块内存空间，这样会占用大量的内存空间，严重影响代码的效率。

```python
words = ['I', ' ', 'love', ' ', 'Python', '.'] 
sentence = ''
for word in words:    
	sentence += '' + word
```

解决这个问题的办法是使用字符串连接的join，Python写法如下：

```python
words = ['I', ' ', 'love', ' ', 'Python', '.'] 
sentence = ''.join(words)
```

#### **4、如何快速翻转字符串**

```python
a = 'I love Python.' 
reverse_a = ''
for i in range(0, len(a)):
	reverse_a += a[len(a) - i - 1]
```

而Python则将字符串看作list，而列表可以通过切片操作来实现反转：

```python
a = 'I love Python.'
reverse_a = a[::-1]
```

#### **5、for/else语句**

```python
cities = ['BeiJing', 'TianJin', 'JiNan', 'ShenZhen', 'WuHan']
tofind = 'Shanghai' 
found = False
for city in cities:
    if tofind == city:        
        print('Found!')        
        found = True        
        break
    if not found:    
        print('Not found!')
```

Python中的通过for…else…会使得代码很简洁，注意else中的代码块仅仅是在for循环中没有执行break语句的时候执行：

```python
cities = ['BeiJing', 'TianJin', 'JiNan', 'ShenZhen', 'WuHan']
tofind = 'Shanghai' 
for city in cities:    
    if tofind == city:        
        print('Found!')        
        break
    else:     
        # 执行else中的语句意味着没有执行break    
        print('Not found!')
```

#### **6、迭代对象善用enumerate类**

enumerate类接收两个参数，其中一个是可以迭代的对象，另外一个是开始的索引。比如，我们想要打印一个列表的索引及其内容，可以用如下代码实现：

```python
cities = ['BeiJing', 'TianJin', 'JiNan', 'ShenZhen', 'WuHan'] 
index = 0
for city in cities:    
    index = index + 1    
    print index, ':', city
```

而通过使用enumerate则极大简化了代码，这里索引设置为从1开始（默认是从0开始）：

```python
cities = ['BeiJing', 'TianJin', 'JiNan', 'ShenZhen', 'WuHan']
for index, city in enumerate(cities, 1):    
    print index, ":", city
```

#### **7、通过lambda来定义函数**

lambda可以返回一个可以调用的函数对象，会使得代码更为简洁。若不使用lambda则需要单独定义一个函数：

```python
def f(x):    
    return x * x 

map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
```

使用lambda后仅仅需要一行代码：

```python
map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9])
```

这里注意，lambda生成的是一个可以像其他函数一样使用的函数对象，即

```python
def f(x):    
    return x * x
```

等价于

```python
lambda x: x * x
```

#### **8、应用上下文管理**

在打开文件时，通常是通过捕获异常来进行实现的，并且在finally模块中对文件来进行关闭：

```python
try:    
    file = open('python.txt')    
    for line in file:        
        print(line)
except:    
    print("File error!")
finally:    
    file.close()
```

而通过上下文管理中的with语句可以让代码非常简洁：

```python
with open('python.txt') as file:    
    for line in file:        
        print(line)
```

#### **9、使用装饰器**

装饰器在Python中应用特别广泛，其特点是可以在具体函数执行之前或者之后做相关的操作，比如：执行前打印执行函数的相关信息，对函数的参数进行校验；执行后记录函数调用的相关流水日志等。使用装饰器最大的好处是**使得函数功能单一化，仅仅处理业务逻辑，而不附带其它功能**。

在函数调用前打印时间函数名相关的信息，不使用装饰器可以用如下代码实现：

```python
from time import ctime 
def foo():    
    print('[%s]  %s() is called' % (ctime(), foo.__name__))    
    print('Hello, Python')
```

这样写的问题是业务逻辑中会夹杂参数检查，日志记录等信息，使得代码逻辑不够清晰。所以，这种场景需要使用装饰器：

```python
from time import ctime 
def deco(func):    
    def decorator(*args, **kwargs):        
        print('[%s]  %s() is called' % (ctime(), func.__name__))        
        return func(*args, **kwargs)    
    return decorator 

@deco
def foo():    
    print('Hello, Python')
```

#### **10、使用生成器**

生成器与列表最大的区别就是，列表是一次性生成的，需要较大的内存空间；而生成器是需要的时候生成的，基本不占用内存空间。生成器分为生成器表达式和生成器函数。

先看一下列表：

```python
l = [x for x in range(10)]
```

改为生成器只需要将[…]变为(…)，即

```python
g = (x for x in range(10))
```

至于生成器函数，是通过yield关键字来实现的，我们以计算斐波那契数列为例，使用列表可以用如下代码来实现：

```python
def fib(max):    
    n, a, b = 0, 0, 1    
    fibonacci = []    
    while n < max:        
        fibonacci.append(b)        
        a, b = b, a + b        
        n = n + 1    
    return fibonacci
```

而使用生成器则变为：

```python
def fib(max):    
    n, a, b = 0, 0, 1    
    while n < max:        
        yield b        
        a, b = b, a + b        
        n = n + 1
```

#### **11、Counter的使用**

通常的词频统计中，我们的思路是：

需要一个字典，key值存储单词，value存储对应的词频。当遇到一个单词，判断是否在这个字典中，如果是，则词频加1；如果否，则字典中新增这个单词，同时对应的词频设置为1。

对应的Python代码实现如下：

```python
#统计单词出现的频次
def computeFrequencies(wordList):    
    #词频字典    
    wordfrequencies = {}     
    for word in wordList:        
        if word not in wordfrequencies:            
            # 单词不在单词词频字典中, 词频设置为1            
            wordfrequencies[word] = 1        
        else:            
            # 单词在单词词频字典中, 词频加1            
            wordfrequencies[word] = wordfrequencies[word]  + 1     
    return wordfrequencies
```

有没有更简单的方式呢？答案是肯定的，就是使用Counter。collection 中的 Counter 类就完成了这样的功能，它是字典类的一个子类。Python代码变得无比简洁：

```python
# 统计单词出现的频次
def computeFrequencies(wordList):    
    #词频字典    
    wordfrequencies = Counter(wordList)    
    return wordfrequencies
```

#### **12、链式比较**

在实际数字比较中，我们可能需要多次比较多次，比如我们判断学习成绩是否位于某个区间：

```python
x = 79 
>>> x < 80 and x > 70
True
```

而更Pythonic的写法变身链式比较，即：

```python
x = 79 
>>> 80 < x < 90
False 
>>> 70 < x < 80
True
```

这种写法给人的感受也更为直观易懂。

#### **13、函数返回多个值**

```python
def f():    
    error_code = 0    
    error_desc = "成功"    
    return error_code, error_desc
```

使用的时候也会非常简单：

```python
code, desc = f()
print code, desc
```

#### **14、使用\*运算符**

*运算符和** 运算符完美的解决了将元组参数、字典参数进行  unpack，从而简化了函数定义的形式，如：

```python
def fun(*args):    
	for eacharg in args:        
		print('tuple arg:', eacharg) 

fun('I', 'love', 'Python')
```

运行的结果为：

tuple arg: I

tuple arg: love

tuple arg: Python

#### **15、找出列表中出现最多的数**

这是经常会遇到的一个问题。解决这个问题的其中一个思路是按照标题11提供的词频统计的方法，先统计词频，然后遍历字典，找出具有最大词频的数字。有没有更简洁的方式？

当然，Python代码如下：

```python
num = [1, 3, 3, 4, 5, 6, 3, 6, 6, 6] 
print(max(set(num),key=num.count))
```

#### 16、if __name__ == ‘__main__’:

让代码既可以被导入又可以被执行。

```python
if __name__ == '__main__':
```

#### 17、判断逻辑“真”或“假”

```python
if x:
if not x:
```

好的代码：

```python
name = 'livre' 
fruits = ['apple', 'orange', 'grape'] 
owners = {'1001': '小三', '1002': '小四'}
if name and fruits and owners:    
    print('I love fruits!')
```

不好的代码：

```python
name = 'livre'
fruits = ['apple', 'orange', 'grape']
owners = {'1001': '小三', '1002': '小四'}
if name != '' and len(fruits) > 0 and owners != {}:    
    print('I love fruits!')
```

#### 18、使用in运算符

```python
if x in items: # 包含
for x in items: # 迭代
```

好的代码：

```python
name = 'LIVRE'
if 'L' in name:    
    print('The name has an L in it.')
```

不好的代码：

```python
name = 'LIVRE'
if name.find('L') != -1:    
    print('This name has an L in it!')
```

#### 19、EAFP优于LBYL

EAFP – Easier to Ask Forgiveness than Permission.

LBYL – Look Before You Leap.

好的代码：

```python
d = {'x': '5'}
try:    
    value = int(d['x'])    
    print(value)
except (KeyError, TypeError, ValueError):    
    value = None
```

不好的代码：

```python
d = {'x': '5'}
if 'x' in d and isinstance(d['x'], str) and d['x'].isdigit():    
    value = int(d['x'])    
    print(value)
else:    
    value = None
```

#### 20、zip组合键和值来创建字典

好的代码：

```python
keys = ['1001', '1002', '1003']
values = ['小二', '小三', '小四']
d = dict(zip(keys, values))
print(d)
```

不好的代码：

```python
keys = ['1001', '1002', '1003']
values = ['小二', '小三', '小四']
d = {}
for i, key in enumerate(keys):    
    d[key] = values[i]
print(d)
```

