from functools import reduce

from ..shared import run


def range_tuples(ranges):
    return [tuple(map(int, i.split("-"))) for i in ranges]


def part2(ranges, _):
    # fmt: off
    return reduce(
        lambda a, r: (s := a[0] - r[1], a[1] + (r[0] - a[2] + 1) * (not s), a[2] if a[0] else r[0]),
        # technically one char shorter
        # lambda a, r: (s := a[0] - r[1], a[1] + (r[0] - a[2] + 1) * (not s), (a + r)[2:][not a[0]]),
        sorted(i for r in range_tuples(ranges) for i in zip(r, [-1, 1])),
        (0, 0, 0),
    )[1]


def part1(ranges, numbers):
    return sum(
        any(e >= i >= s for s, e in rs)
        for rs in [range_tuples(ranges)]
        for i in map(int, numbers)
    )


def main():
    run("test1", part1)
    run("input1", part1)
    run("test1", part2)
    run("test2", part2)
    run("input1", part2)
