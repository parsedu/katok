package lab16

fun soverNum(n: Int): Boolean {
    val arrayNum = setOf(6, 28, 496, 8128, 33550336)
    return n in arrayNum
}
fun main() {
    print("Начало диапазона: ")
    val start = readln().toInt()
    print("Конец диапазона: ")
    val end = readln().toInt()

    println("\nПроверка чисел от $start до $end:")
    var count = 0
    for (num in start..end) {
        val isPerfect = soverNum(num)
        if (isPerfect) {
            println("$num - Господи, ничего совершенее этого числа не видел")
            count++
        } else {
            println("$num - ужас, какое не совершенное число")
        }
    }
}