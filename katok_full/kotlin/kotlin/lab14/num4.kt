package lab14

fun main() {
    val array = arrayOf(
        intArrayOf(1, 2, 3),
        intArrayOf(4, 5, 6),
        intArrayOf(7, 8, 9)
    )

    var max = 0
    var maxRow = -1
    var maxCol = -1

    for (i in array.indices) {
        for (j in array[i].indices) {
            if (array[i][j] > max) {
                max = array[i][j]
                maxRow = i
                maxCol = j
            }
        }
    }

    println("\nМаксимальный элемент: $max")

    if (maxRow == maxCol || maxRow + maxCol == array.size - 1) {
        val doubleMax = max * 2
        if (maxRow == maxCol) {
            for (i in array.indices) {
                array[i][array.size - 1 - i] += doubleMax
            }
        } else {
            for (i in array.indices) {
                array[i][i] += doubleMax
            }
        }
        println("\nМассив после обработки:")
        array.forEach { row ->
            println(row.contentToString())
        }
    }
}
