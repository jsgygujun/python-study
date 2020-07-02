# 数据类型
# 整数： Python可以处理任意大小的整数。
# 浮点数：
# 字符串： 单引号或者双引号括起来的文本，'abc', "xyz"，"I'm OK"。r'xxx'，标示内部的字符串默认不转义。
# 布尔值：True 和 False
# 空值： None，注意None并不是0，而是一个特殊的空值。

# 变量
# a = "ABC"
# 在Python解释器干了两件事情
# 1. 在内存中创建了一个'ABC'字符串；
# 2. 在内存中创建了名为a的变量，并把它指向'ABC'
# 也可以把一个变量a赋值给另一个变量，这个操作实际上是把变量b指向变量a所指向的数据。

# 常量
# Python中用大写的变量名标示常量，如PI=3.141592653589

# 编码
# Python3中，字符串是以Unicode编码的，对于单字符的编码，Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符。
# 由于Python的字符类型是str，在内存中以Unicode表示，一个字符对应若干个字节，如果要在网络上传输，后者保存在磁盘上，就需要把str变为以字节为单位的byte。
# Python对byte类型的数据用带b前缀的单引号或双引号标示：x = b'ABC' 要区分'ABC'和b'ABC'，前者是str，后者虽然内容显示得和前者一样，但是byte的每个字符都只占用一个字节。
# 以Unicode表示的str通过encode()方法可以编码为指定的byte，例如： 'ABC'.encode('ascii'), '中文'.encode('utf-8')
# 纯英文的str可以用ASCII编码为byte，内容是一样的，含有中文的str可以用UTF-8编码为byte，含有中文的str无法用ASCII编码，因为中文的编码范围超过了ASCII编码范围。
# 反过来，如果从网络或者磁盘读取了字节流，那么读到的数据就是byte，要把byte变为str，就需要decode()方法： b'ABC'.decode(
# 'ascii')，b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')

# 格式化
# 'Hello, %s' % 'world'
# 'Hi, %s, you have $%d.' % ('Michael', 10000)

# -*- coding: utf-8 -*-
n = 123
print(n)
f = 456.789
print(f)
s1 = 'Hello, world'
print(s1)
s2 = 'Hello, \'Adam\''
print(s2)
s3 = r'Hello, "Bart"'
print(s3)
s4 = r'''Hello,
Lisa!
'''
print(s4)

# 格式化
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)

# list
classmates = ['Michael', 'Bob', "Tracy"]
print(classmates)
print(len(classmates))  # 长度
classmates.append('Adam')
print(classmates)
classmates.pop()
print(classmates)

# tuple
# 与list相同，唯一不同的就是tuple一旦初始化后，元素就不能改变。
t = (1, 2)
print(t)
t2 = (1,)  # 定义只有一个元素的tuple
print(t2)

# 条件判断
age = 20
if age >= 18:
    print('adult')
elif age >= 6:
    print('teenager')
else:
    print('kid')

# 循环
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

s = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    s = s + x
print(s)


s = 0
for x in range(101):  # range(101)就可以生成0-100的整数序列
    s = s + x
print(s)

s = 0
x = 100
while x > 0:
    s = s + x
    x = x - 1
print(s)

L = ['Bart', 'Lisa', 'Adam']
for name in L:
    print('Hello, %s' % name)


# dict
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}  # 创建字典
print(d['Michael'])
d['Adam'] = 67  # 将'Adam':67 放入d中
print(d)
d.pop('Bob')   # 删除
print(d)

# set
s = {1, 2, 3}  # 创建set
print(s)
s.add(4)  # 增加
s.remove(2)  # 删除
print(s)
