import os

from . import shared

modules = []
module_dir = os.path.realpath(os.path.dirname(__file__))
for i in os.listdir(module_dir):
    if i.startswith("day"):
        modules.append(i)

modules.sort()
for i in modules:
    exec(f"from .{i}.main import main as {i}")


def main():
    for i in modules:
        globals()[i]()
        print("------")


__all__ = ["shared", "main"]
