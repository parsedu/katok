package lab10

import kotlin.math.abs

fun main() {
    val numbers = arrayOf(1, 20, 3, 43, 5, 16, 17, 8, 9, 10)
    print("Массив №1: ")
    for (num in numbers) {
        print("$num ")
    }
    println()
    for (i in numbers.indices) {
        if (abs(numbers[i]) > 10) {
            numbers[i] = 0
        }
    }
    print("Массив№2: ")
    for (num in numbers) {
        print("$num ")
    }
    println()
}