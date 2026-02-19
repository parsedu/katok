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
            if ((i + j) % 2 == 0) {
                if (array[i][j] % 2 == 0) {
                    count++
                }
            }
        }
    }

    println("Количество четных элементов, стоящих на позициях с четной суммой индексов: $count")
}