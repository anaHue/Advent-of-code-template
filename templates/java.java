// Advent of Code __YEAR__ - Day __D__
// Run from the project root:  java java/Day__DD__.java [--example]
import java.nio.file.Files;
import java.nio.file.Path;
import java.util.Arrays;
import java.util.List;
import java.util.function.Function;

public class Day__DD__ {

    static List<String> parse(String raw) {
        return raw.lines().toList();
    }

    static Object part1(List<String> data) {
        return null;
    }

    static Object part2(List<String> data) {
        return null;
    }

    public static void main(String[] args) throws Exception {
        boolean example = Arrays.asList(args).contains("--example");
        String file = example ? "day__DD__.example.txt" : "day__DD__.txt";
        String raw = Files.readString(Path.of("inputs", file)).stripTrailing();

        List<Function<List<String>, Object>> parts = List.of(Day__DD__::part1, Day__DD__::part2);
        for (int i = 0; i < parts.size(); i++) {
            List<String> data = parse(raw);
            long start = System.nanoTime();
            Object result = parts.get(i).apply(data);
            double ms = (System.nanoTime() - start) / 1e6;
            System.out.printf("Part %d: %s  (%.2f ms)%n", i + 1, result, ms);
        }
    }
}
