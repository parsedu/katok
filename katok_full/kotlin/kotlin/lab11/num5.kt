package lab11

import kotlin.math.abs

fun main() {
    val numbers = arrayOf(1, 2, 3, 4, 5, 6,7, 8, -9, 10)
    println("Массив №1: ")
    for (num in numbers) {
        print("$num ")
    }
    println()

    var max = numbers.max()
    var min = numbers.min()
    var proiz = 1
    max /= 2
    min /= 2

    for(i in numbers.indices){
        if ((numbers[i] > min) and (numbers[i] < max)){
            proiz *= numbers[i]
        }
    }

    println("min: $min")
    println("max: $max")

    numbers[numbers.size-2]=proiz;
    numbers.set(0,proiz)
    println("Массив №2: ")
    for (num in numbers) {
        print("$num ")
    }
}

