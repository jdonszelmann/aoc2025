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


def iter_lines(source, strip=True):
    return (i.strip() if strip else i for i in source.split("\n") if i.strip())


def lines(file, strip=True):
    return [iter_lines(*source(file), strip=strip)]


def line_parts(file):
    return [iter_lines(i) for i in source(file)[0].split("\n\n")]


def separated(file, sep=","):
    return [(i.strip() for i in source(file)[0].split(sep) if i.strip())]


commas = partial(separated, sep=",")


def source(file):
    return [open(file).read()]


def name(file):
    return [file]


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
                trans = line_parts

    scriptdir = os.path.dirname(os.path.realpath(str(module.__file__)))
    res = func(*trans(os.path.join(scriptdir, file)))  # pyright: ignore[reportOptionalCall]
    print(f"output for {func.__name__} {file}: {res}")
