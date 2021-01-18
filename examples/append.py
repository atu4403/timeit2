from collections import deque
from timeit2 import ti2


def append_(n):
    li = []
    for i in range(n):
        li.append(i)
    return li


def insert_(n):
    li = []
    for i in range(n):
        li.insert(0, i)
    return li


def deque_right(n):
    li = deque()
    for i in range(n):
        li.append(i)
    return li


def deque_left(n):
    li = deque()
    for i in range(n):
        li.appendleft(i)
    return li


ti2(
    append_,
    insert_,
    deque_right,
    deque_left,
    args=[10 ** 4],
    relative=True,
)

# append_:
#         0.001118 sec
# insert_:
#         0.021187 sec
# deque_right:
#         0.000891 sec
# deque_left:
#         0.000855 sec
# relative:
#         deque_left:
#                 1
#         deque_right:
#                 1.04
#         append_:
#                 1.31
#         insert_:
#                 24.77
