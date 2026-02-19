package lab11

import kotlin.math.abs

fun main() {
    val numbers = arrayOf(11, -22, -33, 44, 55, -66,-77, 88, -99, 10)
    print("Массив №1: ")
    for (num in numbers) {
        print("$num ")
    }
    println()
    var count = 0
    var otric = 0
    for (i in numbers.indices) {
        if (numbers[i] < 0){
            otric += numbers[i]
        }
    }

    for (i in numbers.indices) {
        if (numbers[i] < 0){
            count = i
        break

        }
    }
    val new_numbers = numbers.drop(count).toMutableList()
    println("Новый массив, который начинается с отрицательного элимента$new_numbers")

    for (i in new_numbers.indices){
        if (new_numbers[i] > 0){
            new_numbers[i] = new_numbers[i] * abs(otric)

        }
    }
    println("Индекс первого отрицательного элимента: $count")

    println("Массив№2: ")
for (num in new_numbers) {
    print("$num ")
}
println()
}
