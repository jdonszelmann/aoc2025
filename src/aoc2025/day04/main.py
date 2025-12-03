from ..shared import neighbors, run


def grid(lines):
    return {
        (x, y) for y, line in enumerate(lines) for x, c in enumerate(line) if c == "@"
    }


def movable(g):
    return {c for c in g if sum(n in g for n in neighbors(*c)) < 4}


def iter_movable(g):
    return len(m) + iter_movable(g - m) if (m := movable(g)) else 0


def part2(lines):
    return iter_movable(grid(lines))


def part1(lines):
    return len(movable(grid(lines)))


def main():
    run("test1", part1)
    run("input1", part1)
    run("test1", part2)
    run("input1", part2)
