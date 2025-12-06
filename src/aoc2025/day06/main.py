from functools import reduce

from ..shared import iter_lines, run


def calc(line):
    return reduce(lambda a, b: eval(f"int(a) {line[-1]} int(b)", locals()), line[:-1])


def part2(src):
    return reduce(
        lambda acc, val: (
            (n := val[-1].strip()) or acc[0],
            [*acc[1] * (not n), "".join(val[:-1])],
            acc[2] + calc(n and [*acc[1][:-1], *acc[0]] or [0, 0]),
        ),
        [*zip(*iter_lines(src, False)), *" _"],
        ("", [], 0),
    )[-1]


def part1(lines):
    return sum(
        calc(line)
        for line in zip(
            *[[x.strip() for x in i.split(" ") if x.strip()] for i in lines]
        )
    )


def main():
    run("test1", part1)
    run("input1", part1)
    run("test1", part2)
    run("input1", part2)
