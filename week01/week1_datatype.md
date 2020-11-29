# Python基本数据类型

## 数字

### int

- 不带修饰的整数字面值（包括十六进制、八进制和二进制数）会生成整数
- bool型继承了int型，是int的子类

### float

- 包含小数点或幂运算符的数字字面值会生成浮点数

### complex

- 在数字字面值末尾加上 'j' 或 'J' 会生成虚数（实部为零的复数）

## 序列

### list

- 列表是可变序列，通常用于存放同类项目的集合
- 可以用多种方式构建列表：
使用一对方括号来表示空列表: []
使用方括号，其中的项以逗号分隔: [a], [a, b, c]
使用列表推导式: [x for x in iterable]
使用类型的构造器: list() 或 list(iterable)

### tuple

- 元组是不可变序列，通常用于储存异构数据的多项集
- 可以用多种方式构建元组：
使用一对圆括号来表示空元组: ()
使用一个后缀的逗号来表示单元组: a, 或 (a,)
使用以逗号分隔的多个项: a, b, c or (a, b, c)
使用内置的 tuple(): tuple() 或 tuple(iterable)

### range

- 表示不可变的数字序列，通常用于在 for 循环中循环指定的次数
- 1. class range(stop)
range(10)
2. class range(start, stop[, step])
range(0, 30, 5)

## 文本

### str

- 符串是由 Unicode 码位构成的不可变序列
- 单引号: '允许包含有 "双" 引号'
双引号: "允许包含有 '单' 引号"。
三重引号: '''三重单引号''', """三重双引号"""

## 集合

### set

- set 对象是由具有唯一性的 hashable 对象所组成的无序多项集
- 除了可以使用 set 构造器，非空的 set (不是 frozenset) 还可以通过将以逗号分隔的元素列表包含于花括号之内来创建，例如: {'jack', 'sjoerd'}

### frozenset

- frozenset 类型是不可变并且为 hashable, 其内容在被创建后不能再改变

## 映射

### dict

- mapping 对象会将 hashable 值映射到任意对象。 映射属于可变对象
- 字典可以通过将以逗号分隔的 键: 值 对列表包含于花括号之内来创建，例如: {'jack': 4098, 'sjoerd': 4127} 或 {4098: 'jack', 4127: 'sjoerd'}，也可以通过 dict 构造器来创建。
class dict(**kwarg)
class dict(mapping, **kwarg)
class dict(iterable, **kwarg)

## Other

### 模块

### 类与类实例

### 函数

### 方法

### 代码对象

### 类型对象

### 空对象

### 省略符对象

*XMind - Trial Version*