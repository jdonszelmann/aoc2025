import os
import sys

# fmt: off
oneline = lambda file:(lambda r:r(lambda a,v:(lambda n:(n[0],a[1]+(n[0]==0),a[2]+n[1]))((lambda n,s,i:r(lambda a,_:((a[0]+s)%100,a[1]+((a[0]+s)%100==0),),range(n),(i,0),))(int(v[1:]),(ord(v[0])-79)//3,a[0])),[i for i in open(file).read().split("\n")if i.strip()],(50,0,0),))(__import__("functools").reduce)[1:]

def shared(file):
    at_zero_count = 0
    over_zero_count = 0
    dial = 50

    def simulate(n, s):
        nonlocal dial, over_zero_count, at_zero_count
        for _ in range(n):
            dial += s
            dial %= 100
            if dial == 0:
                over_zero_count += 1
        if dial == 0:
            at_zero_count += 1

    for i in [i for i in open(file).read().split("\n") if i.strip() != ""]:
        simulate(int(i[1:]), {"L": -1, "R": +1}[i[0]])

    return at_zero_count, over_zero_count


shared = oneline


def part1(file):
    return shared(file)[0]


def part2(file):
    return shared(file)[1]


def run(file, func):
    scriptdir = os.path.dirname(os.path.realpath(sys.argv[0]))
    res = func(os.path.join(scriptdir, file))
    print(f"output for {func.__name__} {file}: {res}")


def main():
    run("test1", part1)
    run("part1", part1)
    run("test1", part2)
    run("part1", part2)


if __name__ == "__main__":
    main()
