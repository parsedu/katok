package lab12

fun main() {
    val array = arrayOf(
        arrayOf(5, -3, 8),
        arrayOf(-1, 0, -7),
        arrayOf(2, -4, 6)
    )


    var count = 0

    for (i in array.indices) {
        for (j in array[i].indices) {
            if (array[i][j] % (i + 1) == 0 || array[i][j] % (j + 1) == 0) {
                count++
            }
        }
    }

    println("Количество элементов, которые делятся без остатка на свой индекс (строки или столбца): $count")
}