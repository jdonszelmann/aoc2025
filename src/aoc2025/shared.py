import inspect
import os
from functools import partial


def neighbors(x, y):
    return [
        (x + dx, y + dy)
        for dx in range(-1, 2)
        for dy in range(-1, 2)
        if not (dx == dy == 0)
    ]


def print_map(x):
    print(x)
    return x


def lines(file):
    yield from (i.strip() for i in source(file).split("\n") if i.strip())


def separated(file, sep=","):
    yield from (i.strip() for i in source(file).split(sep) if i.strip())


commas = partial(separated, sep=",")


def source(file):
    return open(file).read()


def name(file):
    return file


def run(file, func, trans=None):
    module = inspect.getmodule(func)
    if module is None:
        exit("couldn't determine module")

    if trans is None:
        sig = inspect.signature(func)
        match tuple(sig.parameters.keys()):
            case ():
                exit("expected one argument")
            case ("lines",):
                trans = lines
            case ("file",):
                trans = name
            case (_,) if "sep" in func.__code__.co_varnames:
                trans = partial(separated, sep=func.__code__.co_consts[0])
            case ("src" | "source" | _,):
                trans = source
            case (_, _, *_):
                exit("too many parameters")

    scriptdir = os.path.dirname(os.path.realpath(str(module.__file__)))
    res = func(trans(os.path.join(scriptdir, file)))  # pyright: ignore[reportOptionalCall]
    print(f"output for {func.__name__} {file}: {res}")
