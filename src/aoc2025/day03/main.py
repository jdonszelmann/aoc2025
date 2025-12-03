from functools import reduce

from ..shared import run


def argmax(line):
    return max(range(len(line)), key=lambda x: line[x])


def largest(i, n, r):
    return [
        reduce(
            lambda e, d: [m := argmax(e[: len(e) - d + 1]), r.append(e[m]), e[m + 1 :]][
                -1
            ],
            range(n, 0, -1),
            i,
        ),
        int("".join(r)),
    ][-1]


def part1(lines):
    return sum(largest(line, 2, []) for line in lines)


def part2(lines):
    return sum(largest(line, 12, []) for line in lines)


def main():
    run("test1", part1)
    run("part1", part1)
    run("test1", part2)
    run("part1", part2)
