from timeit2 import ti2


def f():
    li = []
    for i in range(10 ** 5):
        li.append(i * i)
    return li


ti2(f)

# f:
#         0.015094 sec
