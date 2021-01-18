from timeit2 import ti2

arg = range(10 ** 6)
ti2(
    max,
    sum,
    args=[arg],
    floor=4,
    print_return=True,
    return_label="ret: ",
    relative=True,
)

# max:
#         0.0360 sec
#         ret: 999999
# sum:
#         0.0266 sec
#         ret: 499999500000
# relative:
#         sum:
#                 1
#         max:
#                 1.36
