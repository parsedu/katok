package lab14

import kotlin.math.pow

fun main() {
    val array = arrayOf(
        arrayOf(5, -3, 8),
        arrayOf(-1, 0, -7),
        arrayOf(2, -4, 6)
    )

    val diagSum = array.indices.sumOf { array[it][it] }
    val dubDiagSum = array.indices.sumOf { array[it][array.size - 1 - it] }

    println("Сумма главной диагонали: $diagSum")
    println("Сумма побочной диагонали: $dubDiagSum")
    if (diagSum > dubDiagSum) {
        val diff = diagSum - dubDiagSum
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