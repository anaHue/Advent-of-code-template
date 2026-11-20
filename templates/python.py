#!/usr/bin/env python3
"""Advent of Code __YEAR__ - Day __D__"""
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def read_input(example=False):
    name = "day__DD__.example.txt" if example else "day__DD__.txt"
    return (ROOT / "inputs" / name).read_text().rstrip("\n")


def parse(raw):
    return raw.splitlines()


def part1(data):
    return None


def part2(data):
    return None


def main():
    example = "--example" in sys.argv or "-e" in sys.argv
    raw = read_input(example)
    for n, fn in ((1, part1), (2, part2)):
        data = parse(raw)  # fresh copy so parts can't mutate each other's input
        start = time.perf_counter()
        result = fn(data)
        ms = (time.perf_counter() - start) * 1000
        print(f"Part {n}: {result}  ({ms:.2f} ms)")


if __name__ == "__main__":
    main()
