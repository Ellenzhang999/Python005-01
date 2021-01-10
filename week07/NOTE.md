
# 作业
## 作业一：区分以下类型哪些是容器序列哪些是扁平序列，哪些是可变序列哪些是不可变序列：
list
tuple
str
dict
collections.deque

### Answer：
扁平序列：str
容器序列：list，tuple，dict，collections.deque
可变序列：list，dict，collections.deque
不可变序列：tuple

## 作业二：
自定义一个 python 函数，实现 map() 函数的功能。

Answer: task1_map.py

map()函数
它是python内置的高阶函数 , 接收一个函数 f 和一个 list , 并通过把函数 f 依次作用在 list 的每个元素上 , 得到一个新的list 并返回实例

## 作业三：
实现一个 @timer 装饰器，记录函数的运行时间，注意需要考虑函数可能会接收不定长参数。

Answer: task2_map.py

# 学习笔记
## 变量赋值
可变数据类型：dict，list
不可变数据类型：int，float，string，tuple
容器序列：list、tuple、collections.deque 等，能存放不同类型的数据 容器序列可以存放不同类型的数据。
扁平序列：str、bytes、bytearray、memoryview (内存视图)、array.array 等，存放的是相同类型的数据 扁平序列只能容纳一种类型。
可变序列 list、bytearray、array.array、collections.deque 和 memoryview。
不可变序列 tuple、str 和 bytes。

容器序列存在深拷贝、浅拷贝问题

## 作用域
Python 和高级语言有很大差别，在模块、类、函数中定义，才有作用域的概念。
Python 作用域遵循 LEGB 规则。
LEGB 含义解释：
• L-Local(function)；函数内的名字空间
• E-Enclosing function locals；外部嵌套函数的名字空间（例如closure） 
• G-Global(module)；函数定义所在模块（文件）的名字空间
• B-Builtin(Python)；Python 内置模块的名字空间

## 容器数据类型
list, dict, set, tuple
https://docs.python.org/zh-cn/3.7/library/collections.html

## 内置装饰器
在functiontools的标准库中
functools.wraps的作用，就是给被修饰的函数的一些属性值赋值给修饰器函数。
functools.lru_cache(maxsize=128, typed=False)有两个可选参数 # maxsize代表缓存的内存占用值，超过这个值之后，就的结果就会被释放
推荐阅读《fluent python》

## 类装饰器
类要实现__call__的方法，第一个参数是self

## 官方文档中的装饰器
Data class：https://www.python.org/dev/peps/pep-0557/

## 对象协议与鸭子类型
容器类型协议
1. __str__ 打印对象时，默认输出该方法的返回值
2. __getitem__, __setitem__, __delitem__ 字典索引操作
3. __iter__ 迭代器
4. __call__ 可调用对象协议
比较大小的协议：__eq__, etc.
描述符协议和属性交互协议 __get__, etc.
可哈希对象 __hash__

格式化字符串
typing类型注解：type hint，不做强制类型约束，只是一种提示

## Yield
生成器：
1. iterable：包含__getitem__()或__iter__()方法的容器对象
2. iterator：包含next()和__iter__()方法
3. Generator：包含yield语句的函数
Iter就是可以用for in来操作；如果是iterable并且包括了next()方法，就是iterator；如果再包含yield语句，就是Generator。
生成器实现了完整的迭代器操作

## 迭代器使用的注意事项
无限迭代器

## Yield表达式
使用next或者send将yield的暂停状态变成继续

## 异步编程
协程与同步的区别
async await
