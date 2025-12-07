from collections import Counter as C
from functools import reduce

from ..shared import run


def grid(lines):
    return [{x for x, c in enumerate(line) if c != "."} for line in lines]


def group(items):
    return


def part2(lines):
    g = grid(lines)
    return sum(
        reduce(
            lambda a, v: sum(
                (
                    C({x + 1: c, x - 1: c}) if x in v else C({x: c})
                    for x, c in a.items()
                ),
                C(),
            ),
            g[1:],
            {g[0].pop(): 1},
        ).values()
    )


def part1(lines):
    g = grid(lines)
    return reduce(
        lambda a, v: (
            {x for i in a[0] for x in ([i + 1, i - 1] if i in v else [i])},
            a[1] + sum(i in v for i in a[0]),
        ),
        g[1:],
        (set(g[0]), 0),
    )[1]


def main():
    run("test1", part1)
    run("input1", part1)
    run("test1", part2)
    run("input1", part2)
