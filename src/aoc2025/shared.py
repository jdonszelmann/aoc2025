import inspect
import os


def print_map(x):
    print(x)
    return x


def lines(file):
    yield from (i.strip() for i in source(file).split("\n") if i.strip())


def commas(file):
    yield from (i.strip() for i in source(file).split(",") if i.strip())


def source(file):
    return open(file).read()


def name(file):
    return file


def run(file, func, trans=name):
    module = inspect.getmodule(func)
    if module is None:
        exit("couldn't determinte module")

    scriptdir = os.path.dirname(os.path.realpath(str(module.__file__)))
    res = func(trans(os.path.join(scriptdir, file)))
    print(f"output for {func.__name__} {file}: {res}")
