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
            if (array[i][j] % 3 == 2) {
                count++
            }
        }
    }

    println("Количество элементов, которые при делении на 3 дают остаток 2: $count")
}