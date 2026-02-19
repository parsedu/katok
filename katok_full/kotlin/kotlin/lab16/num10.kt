package lab16

fun sozdastArray(a: Int, b: Int): IntArray {
    val start: Int
    val end: Int

    if (a < b) {
        start = a
        end = b
    } else {
        start = b
        end = a
    }

    val size = end - start + 1
    val result = IntArray(size)

    for (i in 0 until size) {
        result[i] = start + i
    }

    return result
}

fun main() {
    println("Введите два числа:")

    val (num1, num2) = readln().split(" ").map { it.toInt() }
    val result = sozdastArray(num1, num2)

    println("\nРезультат:")
    println("От: ${minOf(num1, num2)}")
    println("До: ${maxOf(num1, num2)}")
    println("Массив: ${result.joinToString(", ", "[", "]")}")
}