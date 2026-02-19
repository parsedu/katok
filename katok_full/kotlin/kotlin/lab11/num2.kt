package lab11

import kotlin.math.abs

fun main() {
    val numbers = arrayOf(1, -2, -3, -4, 5, -6,-7, 8, -9, 10)
    print("Массив №1: ")
    for (num in numbers) {
        print("$num ")
    }
    println()
    var count = 0
    var otric =1
    for (i in numbers.indices) {
        if (numbers[i] < 0){
            otric = otric * numbers[i]
            count++
            if (count >2){
                break
            }
        }
    }

    for(i in numbers.indices){
        if ( numbers[i] % 2 !=0){
            numbers[i]=otric
        }
    }
    println("Сумма первых трех отриц: $otric")

    println("Массив №2: ")
    for (num in numbers) {
        print("$num ")
    }
    println()




}
