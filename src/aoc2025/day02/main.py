from ..shared import run


def bad_part1(id, n=2):
    return not (
        len(id) % n
        or len({str(id)[i : i + len(id) // n] for i in range(0, len(id), len(id) // n)})
        - 1
    )


def bad_part2(id):
    return any(bad_part1(id, n) for n in reversed(range(2, len(id) + 1)))


def shared(ranges, bad):
    return sum(
        id
        for start, end in (r.split("-") for r in ranges)
        for id in range(int(start), int(end) + 1)
        if bad(str(id))
    )


def part1(ranges):
    sep = ","  # pyright: ignore[reportUnusedVariable]
    return shared(ranges, bad_part1)


def part2(ranges):
    sep = ","  # pyright: ignore[reportUnusedVariable]
    return shared(ranges, bad_part2)


def main():
    run("test1", part1)
    run("part1", part1)
    run("test1", part2)
    run("part1", part2)
