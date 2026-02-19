package lab16

fun prostoeCh(n: Int): Boolean {
    if (n <= 1) return false
    if (n == 2) return true
    if (n % 2 == 0) return false

    for (i in 3..Math.sqrt(n.toDouble()).toInt() step 2) {
        if (n % i == 0) return false
    }

    return true
}

fun main() {
    print("Начало: ")
    val start = readln().toInt()
    print("Конец: ")
    val end = readln().toInt()

    var count = 0
    for (num in start..end) {
        val numb = prostoeCh(num)
        if (numb) {
            println("$num - Простое")
            count++
        } else {
            println("$num - Составное")
        }
    }
    println("\nНайдено простых чисел: $count")
}