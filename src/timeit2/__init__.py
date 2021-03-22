import time
import copy
from typing import Callable


def ti2(
    *fn: Callable,
    args: list = [],
    number: int = 100,
    floor: int = 6,
    relative: bool = False,
    print_return: bool = False,
    return_label: str = "",
):
    """Extended version of timeit package

    Args:
        fn (Callable): Time measuring function
        args (list, optional): argument of fn. Defaults to [].
        number (int, optional): Time measuring count number. Defaults to 100.
        floor (int, optional): Number after the decimal point. Defaults to 6.
        relative (bool, optional): Print relative evaluation. Defaults to False.
        print_return (bool, optional): Print the return value. Defaults to False.
        return_label (str, optional): Return value label. Defaults to "".

    Returns:
        list[tuple]: list of measured times
    """
    times = []
    for f in fn:
        fres = {"name": f.__name__, "results": [], "times": []}
        for _ in range(number):
            _args = copy.deepcopy(args)
            start = time.perf_counter()
            fres["results"].append(f(*_args))
            fres["times"].append(time.perf_counter() - start)
        t = fres["times"]
        fres["fast"] = min(t)
        times.append(
            (
                fres["name"],
                fres["fast"],
            )
        )
        print(f"{fres['name']}:\n\t{fres['fast']:.{floor}f} sec")
        if print_return:
            r = fres["results"][0]
            print(f"\t{return_label}{fres['results'][0]}")
    if relative:
        times.sort(key=lambda x: x[1])
        first = True
        base = -1.0
        for t in times:
            if first:
                base = t[1]
                print(f"relative:\n\t{t[0]}:\n\t\t1")
                first = False
            else:
                r = t[1] / base
                print(f"\t{t[0]}:\n\t\t{r:.2f}")
    return times


ti = ti2
timeit = ti2
timeit2 = ti2
