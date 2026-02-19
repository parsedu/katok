package lab11

import kotlin.math.abs

fun main() {
    val numbers = arrayOf(1, 2, 3, 4, 5, 6,7, 8, -9, 10)
    println("Массив №1: ")
    for (num in numbers) {
        print("$num ")
    }
    println()

    var max = numbers.maxOrNull()
    var min = numbers.minOrNull()
    var avg = numbers.average()

    for(i in numbers.indices){
        if (numbers[i]<avg){
            numbers[i]= numbers[i] * numbers[i]
        }
    }

    println("min: $min")
    println("max: $max")
    println("avg: $avg")

    println("Массив №2: ")
    for (num in numbers) {
        print("$num ")
    }
    println()
}

