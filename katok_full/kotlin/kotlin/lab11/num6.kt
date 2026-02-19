package lab11

import kotlin.math.abs

fun main() {
    val numbers = arrayOf(1, 2, 3, 4, 5, 6,7, 8, -9, 10)
    println("Массив №1: ")
    for (num in numbers) {
        print("$num ")
    }
    println()
    var count = 0
    var max = numbers.max()
    for(i in numbers.indices){
        if (numbers[i] %2 == 0){
            count++
        }
    }
    println("max: $max")
    max = max * count
    println("max: $max")

    println("Массив №2: ")
    for (num in numbers) {
        print("$num ")
    }
}

