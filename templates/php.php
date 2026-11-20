<?php
// Advent of Code __YEAR__ - Day __D__
// Run from anywhere:  php php/day__DD__.php [--example]

$example = in_array('--example', $argv) || in_array('-e', $argv);
$file = $example ? 'day__DD__.example.txt' : 'day__DD__.txt';
$raw = rtrim(file_get_contents(__DIR__ . '/../inputs/' . $file));

function parse(string $raw): array
{
    return explode("\n", $raw);
}

function part1(array $data)
{
    return null;
}

function part2(array $data)
{
    return null;
}

foreach (['part1', 'part2'] as $i => $fn) {
    $data = parse($raw); // fresh copy per part
    $start = hrtime(true);
    $result = $fn($data);
    $ms = (hrtime(true) - $start) / 1e6;
    printf("Part %d: %s  (%.2f ms)\n", $i + 1, var_export($result, true), $ms);
}
