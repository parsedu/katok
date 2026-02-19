package lab14

import kotlin.math.pow

fun main() {

    val array = arrayOf(
        arrayOf(1, 2, 3),
        arrayOf(4, 5, 6),
        arrayOf(7, 8, 9)
    )
    println("Исходный массив A:")
    array.forEach { row -> println(row.contentToString()) }

    val digSum = array.indices.sumOf { array[it][it] }
    val secdig = array.indices.sumOf { array[it][array.size - 1 - it] }

    println("Сумма главной диагонали: $digSum")
    println("Сумма побочной диагонали: $secdig")

    if (digSum > secdig) {
        val diff = digSum - secdig
        val diffS = diff.toDouble().pow(2.0)

        for (i in array.indices) {
            val j = array.size - 1 - i
            if (array[i][j] < 0) {
                array[i][j] = diffS.toInt()
            }
        }

        println("Массив A после замены отрицательных элементов под побочной диагональю:")
        array.forEach { row -> println(row.contentToString()) }

    } else {
        println("Сумма главной диагонали не превышает сумму побочной, изменения не производятся.")
    }
}