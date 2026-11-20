# Advent of Code

## Layout
```
inputs/      dayNN.txt (your puzzle input), dayNN.example.txt (sample from the puzzle text)
python/ js/ java/ kotlin/ php/   one file per day
templates/   the blank templates new_day.py copies from
new_day.py   scaffolding script
```

## Start a day
```
python new_day.py 1 python            # one language
python new_day.py 1 python kotlin     # several
python new_day.py 1                   # all languages
python new_day.py 1 python --fetch    # also download input (export AOC_SESSION=<cookie> first)
```
Paste the sample into `inputs/day01.example.txt` and (if not fetched) your input into `inputs/day01.txt`.

## Run (from the project root)
| Language | Command | Needs |
|---|---|---|
| Python | `python python/day01.py [--example]` | 3.8+ |
| JS | `node js/day01.js [--example]` | Node 16+ |
| Java | `java java/Day01.java [--example]` | JDK 17+ |
| PHP | `php php/day01.php [--example]` | PHP 8.1+ |
| Kotlin | `kotlinc kotlin/Day01.kt -include-runtime -d out/day01.jar && java -jar out/day01.jar [--example]` | kotlinc + JDK |

Each prints both parts with timings. Workflow: get the example right with `--example`, then run on the real input.

## Getting your session cookie (for --fetch)
Log in at adventofcode.com, open dev tools -> Application/Storage -> Cookies, copy the value of `session`.
Keep it private; it is your login.
