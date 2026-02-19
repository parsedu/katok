package lab14

fun main() {
    val array = arrayOf(
        arrayOf(-1, -2, 3, -4),
        arrayOf(-5, 6, -7, 8),
        arrayOf(-9, -10, -11, -12),
        arrayOf(13, -14, -15, 16)
//    val array = arrayOf(
//        arrayOf(1, -2, 3, -4),
//        arrayOf(5, 6, -7, 8),
//        arrayOf(-9, 10, 11, -12),
//       arrayOf(13, -14, 15, 16)
    )
    val n = 4

    var posC = 0
    for (i in 0 until n) {
        for (j in 0 until n) {
            if (array[i][j] > 0) {
                posC++
            }
        }
    }

    println("Количество положительных элементов: $posC")

    if (posC > n * n / 2) {
        var maxA = -999
        var maxB = -999
        var posA = Pair(-1, -1)
        var posB = Pair(-1, -1)

        for (i in 0 until n) {
            for (j in i + 1 until n) {
                if (array[i][j] > maxA) {
                    maxA = array[i][j]
                    posA = Pair(i, j)
                }
            }
        }

        for (i in 0 until n) {
            for (j in 0 until i) {
                if (array[i][j] > maxB) {
                    maxB = array[i][j]
                    posB = Pair(i, j)
                }
            }
        }

        if (posA.first != -1 && posB.first != -1) {
            array[posA.first][posA.second] = maxB
            array[posB.first][posB.second] = maxA
            println("Изменены элементы: [${posA.first},${posA.second}] = $maxA и [${posB.first},${posB.second}] = $maxB")
        }
    } else {

        for (i in 0 until n) {
            for (j in 0 until n) {
                if (array[i][j] < 0) {
                    array[i][j] = array[i][j] * array[i][j]
                }
            }
        }
        println("Все отрицательные элементы возведены в квадрат")
    }
    array.forEach { row -> println(row.contentToString()) }
}
