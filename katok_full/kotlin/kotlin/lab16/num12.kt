package lab16

fun kakoitoFinabichi(n: Int): Long {
    if (n <= 0) return 0L
    if (n == 1) return 1L

    val fib = LongArray(n)
    fib[0] = 1L
    fib[1] = 1L

    for (i in 2 until n) {
        fib[i] = fib[i - 1] + fib[i - 2]
    }

    return fib.sum()
}

fun main() {
    println("Введите N:")
    val n = readln().toInt()

    val sum = kakoitoFinabichi(n)
    println("Сумма первых $n чисел Фибоначчи: $sum")
}