// Advent of Code __YEAR__ - Day __D__
// Run from the project root:
//   kotlinc kotlin/Day__DD__.kt -include-runtime -d out/day__DD__.jar && java -jar out/day__DD__.jar [--example]
import java.io.File
import kotlin.system.measureNanoTime

fun parse(raw: String): List<String> = raw.lines()

fun part1(data: List<String>): Any? {
    return null
}

fun part2(data: List<String>): Any? {
    return null
}

fun main(args: Array<String>) {
    val example = "--example" in args
    val file = if (example) "day__DD__.example.txt" else "day__DD__.txt"
    val raw = File("inputs/$file").readText().trimEnd()

    listOf(::part1, ::part2).forEachIndexed { i, fn ->
        val data = parse(raw)
        var result: Any? = null
        val ns = measureNanoTime { result = fn(data) }
        println("Part ${i + 1}: $result  (${"%.2f".format(ns / 1e6)} ms)")
    }
}
