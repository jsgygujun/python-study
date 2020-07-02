# 定义函数
import math


def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x


print(my_abs(-23))


# 定义空函数
def nop():
    pass


# 参数检查
def my_abs_2(x):
    if not isinstance(x, (int, float)):
        raise TypeError("Bad operand type")  # 抛出异常
    return my_abs(x)


# print(my_abs_2('244'))


# 返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x_, y_ = move(100, 100, 60, math.pi / 6.)
print(x_, y_)


# 函数的参数
# 默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5))
print(power(5, 3))


# 可变参数
def calc(*nums):
    s = 0
    for n in nums:
        s = s + n
    return s


print(calc(1, 2))
print(calc(1))
print(calc(1, 3, 4, 5))
x_ = [1, 2, 3]
print(calc(*x_))  # 将list作为可变参数传进去


# 关键字参数
def person(name, age, **kw):
    print('name: %s, age: %d, other: %s' % (name, age, kw))


person('Michael', 30)
person('Adam', 45, gender='M', job='Engineer')
d = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, **d)
