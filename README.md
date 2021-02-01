# timeit2 


このパッケージは処理時間の計測module [timeit](https://docs.python.org/3/library/timeit.html) を使いやすくしたものです。以下の特徴があります。

- 引数を使い回しません(timeitは引数を書き換える処理をした時にそのまま次に渡します)
- 複数の関数を1度に計測して相対的な速度差を視覚化できます
- 処理時間の桁数を変えられます(0.00374567より0.0037の方が見やすい)
- 返り値を一緒にprintできます

![test](https://github.com/atu4403/timeit2/workflows/test/badge.svg)


## Install

```
$ pip install timeit2
```


## Example

```python
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
#         0.0356 sec
#         ret: 999999
# sum:
#         0.0249 sec
#         ret: 499999500000
# relative:
#         sum:
#                 1
#         max:
#                 1.43
```

最小限の使い方

```python
from timeit2 import ti2

def f():
    li = []
    for i in range(10 ** 5):
        li.append(i * i)
    return li

ti2(f)

# f:
#         0.015094 sec
```

配列作成に`list.append`,`list.insert`,`deque`をそれぞれ使った処理時間と相対評価

```python
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
```

## API

```python
ti2(
    *fn: Callable,
    args: list = [],
    number: int = 100,
    floor: int = 6,
    relative: bool = False,
    print_return: bool = False,
    return_label: str = "",
)
```

### argument

#### fn

Type: Callable

計測する関数、可変長引数なので複数指定が可能。
引数がある場合は`args=` で指定する。

### Options

#### args 

Type: list

Default: []

fnに渡す引数のlist

#### number 

Type: int

Default: 100

各関数を計測する回数、結果はその最速値が表示される


#### floor

Type: int

Default: 6

表示する小数点以下の桁数


#### relative

Type: bool

Default: False

計測結果に相対評価を追加する

#### print_return

Type: bool

Default: False

計測結果に関数の返り値を追加する

#### return_label

Type: str
Default: ""

`print_return=True`の場合、返り値のラベルを指定する


## alias

ti2, ti, timeit, timeit2 をimportできますが、全て同じものです。


```python
from timeit2 import ti2, ti, timeit, timeit2
```

## Related
- [timeit](https://docs.python.org/3/library/timeit.html)


## License

MIT © 2021 [atu4403](https://github.com/atu4403)
