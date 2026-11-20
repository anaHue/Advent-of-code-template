// Advent of Code __YEAR__ - Day __D__
// Run from anywhere:  node js/day__DD__.js [--example]
const fs = require("fs");
const path = require("path");

const example = process.argv.includes("--example") || process.argv.includes("-e");
const file = example ? "day__DD__.example.txt" : "day__DD__.txt";
const raw = fs.readFileSync(path.join(__dirname, "..", "inputs", file), "utf8").trimEnd();

const parse = (raw) => raw.split("\n");

const part1 = (data) => {
  return null;
};

const part2 = (data) => {
  return null;
};

[part1, part2].forEach((fn, i) => {
  const data = parse(raw); // fresh copy per part
  const start = performance.now();
  const result = fn(data);
  console.log(`Part ${i + 1}: ${result}  (${(performance.now() - start).toFixed(2)} ms)`);
});
