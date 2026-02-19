package lab11

import kotlin.math.abs

fun main() {
    val numbers = arrayOf(1, -2, -3, -4, 5, -6,-7, 8, -9, 10)
    println("Массив №1: ")
    for (num in numbers) {
        print("$num ")
    }
    println()
    var count = 0
    var otric =1
    for (i in numbers.indices) {
        if ((i+1) %2 !=0){
            if (otric< numbers[i]){
                otric = numbers[i]
            }
        }
    }

    for(i in numbers.indices){
        if ((i+1) %2 ==0){
            numbers[i]=numbers[i] - otric
        }
    }
    println("Наибольший элимент на нечетных поз: $otric")

    println("Массив №2: ")
    for (num in numbers) {
        print("$num ")
    }
    println()
}

