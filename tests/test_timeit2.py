from timeit2 import ti2, ti, timeit, timeit2


def fn1(n):
    for i in range(10 ** 4):
        pass
    return 1


def fn2(n):
    return 1


def fn3(n):
    for i in range(10 ** 3):
        pass
    return 1.2


def test_full_args(mocker):
    mocker.patch("builtins.print")
    f1 = mocker.MagicMock(side_effect=fn1)
    f2 = mocker.MagicMock(side_effect=fn2)
    f3 = mocker.MagicMock(side_effect=fn3)
    f1.__name__ = "f1"
    f2.__name__ = "f2"
    f3.__name__ = "f3"
    a = ti2(
        f1,
        f2,
        f3,
        args=[9],
        number=1000,
        print_return=True,
        floor=7,
        return_label="return: ",
        relative=True,
    )
    assert f1.call_count == 1000
    assert f2.call_count == 1000
    assert f3.call_count == 1000
    assert print.call_count == 9
    assert a[0][1] <= a[1][1] <= a[2][1]
    assert a[0][0] == "f2" and a[1][0] == "f3" and a[2][0] == "f1"


def test_number(mocker):
    mocker.patch("builtins.print")
    ti(fn1, args=[100], number=1)
    assert print.call_count == 1


def test_alias(mocker):
    mocker.patch("builtins.print")
    ti(fn2, args=[1], number=3) == ti2(fn2, args=[1], number=3) == timeit(
        fn2, args=[1], number=3
    ) == timeit2(fn2, args=[1], number=3)
