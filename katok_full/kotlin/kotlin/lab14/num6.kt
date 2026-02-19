package lab14
fun main() {
    val array = arrayOf(
        arrayOf(1, 2, 30, 4),
        arrayOf(5, 6, 7, 8),
        arrayOf(9, 10, 11, 12),
        arrayOf(13, 1, 15, 16)
    )

    val n = array.size

    var sumAbove = 0.0
    for (i in 0 until n) {
        for (j in i + 1 until n) {
            sumAbove += array[i][j]
        }
    }

    var sumBelow = 0.0
    for (i in 1 until n) {
        for (j in 0 until i) {
            sumBelow += array[i][j]
        }
    }

    var minSide = array[0][n - 1]
    var maxSide = array[0][n - 1]

    for (i in 0 until n) {
        val j = n - 1 - i
        if (array[i][j] < minSide) minSide = array[i][j]
        if (array[i][j] > maxSide) maxSide = array[i][j]
    }

    if (sumAbove > sumBelow) {
        for (i in 0 until n) {
            val j = n - 1 - i
            if (array[i][j] == maxSide) {
                array[i][j] *= 2
                break
            }
        }
        println("\nСумма над диагональю ($sumAbove) > суммы под диагональю ($sumBelow)")
        println("Максимальный элемент на побочной диагонали ($maxSide) умножен на 2")
    } else {
        for (i in 0 until n) {
            val j = n - 1 - i
            if (array[i][j] == minSide) {
                array[i][j] *= array[i][j]
                break
            }
        }
        println("\nСумма над диагональю ($sumAbove) <= суммы под диагональю ($sumBelow)")
        println("Минимальный элемент на побочной диагонали ($minSide) возведен в квадрат")
    }
    println("\nМассив после преобразования:")
    for (i in 0 until n) {
        for (j in 0 until n) {
            print("${array[i][j]}\t")
        }
        println()
    }
}