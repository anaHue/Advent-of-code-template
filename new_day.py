#!/usr/bin/env python3
"""Scaffold an Advent of Code day.

Usage:
  python new_day.py [day] [lang ...] [--year YEAR] [--fetch]

  day      1-25 (default: today's day of the month)
  lang     python | js | java | kotlin | php | all   (default: all)
  --fetch  download your puzzle input (needs env var AOC_SESSION = your session cookie)

Examples:
  python new_day.py 1 python
  python new_day.py 5 python kotlin --fetch
  python new_day.py            # today, all languages
"""
import argparse
import datetime
import os
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LANGS = {  # lang: (template, output dir, filename pattern)
    "python": ("python.py", "python", "day{DD}.py"),
    "js": ("js.js", "js", "day{DD}.js"),
    "java": ("java.java", "java", "Day{DD}.java"),
    "kotlin": ("kotlin.kt", "kotlin", "Day{DD}.kt"),
    "php": ("php.php", "php", "day{DD}.php"),
}


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("day", nargs="?", type=int, default=datetime.date.today().day)
    p.add_argument("langs", nargs="*", default=["all"])
    p.add_argument("--year", type=int, default=datetime.date.today().year)
    p.add_argument("--fetch", action="store_true")
    a = p.parse_args()

    langs = list(LANGS) if "all" in a.langs else a.langs
    for l in langs:
        if l not in LANGS:
            p.error(f"unknown language '{l}' (choose from {', '.join(LANGS)}, all)")

    dd = f"{a.day:02d}"
    subs = {"__DD__": dd, "__D__": str(a.day), "__YEAR__": str(a.year)}

    for l in langs:
        tpl, folder, pattern = LANGS[l]
        out = ROOT / folder / pattern.format(DD=dd)
        if out.exists():
            print(f"skip   {out.relative_to(ROOT)} (already exists)")
            continue
        text = (ROOT / "templates" / tpl).read_text()
        for k, v in subs.items():
            text = text.replace(k, v)
        out.parent.mkdir(exist_ok=True)
        out.write_text(text)
        print(f"create {out.relative_to(ROOT)}")

    inputs = ROOT / "inputs"
    inputs.mkdir(exist_ok=True)
    example = inputs / f"day{dd}.example.txt"
    real = inputs / f"day{dd}.txt"
    example.touch(exist_ok=True)

    if a.fetch and not real.exists():
        session = os.environ.get("AOC_SESSION")
        if not session:
            print("fetch  skipped: set AOC_SESSION to your adventofcode.com session cookie")
        else:
            req = urllib.request.Request(
                f"https://adventofcode.com/{a.year}/day/{a.day}/input",
                headers={"Cookie": f"session={session}", "User-Agent": "personal AoC scaffold script"},
            )
            real.write_bytes(urllib.request.urlopen(req).read())
            print(f"fetch  {real.relative_to(ROOT)}")
    elif not real.exists():
        real.touch()
        print(f"create {real.relative_to(ROOT)} (paste your puzzle input here)")


if __name__ == "__main__":
    main()
