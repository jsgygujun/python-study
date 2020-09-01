def f(x):
    return x * x


r = map(f, [x for x in range(1, 10)])
print(list(r))
