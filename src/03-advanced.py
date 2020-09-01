L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:3])  # 取前3个
print(L[:3])  # 取前3个
print(L[-3:])  # 取后3个


d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)


L = list(range(1, 11))
print(L)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

L = [x*x for x in range(1, 11)]
print(L)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

