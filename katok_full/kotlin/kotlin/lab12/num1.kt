package lab12

fun main() {
    val array = arrayOf(
        arrayOf(5, -3, 8),
        arrayOf(-1, 0, -7),
        arrayOf(2, -4, 6)
    )


    var sum = 0
    for (i in array.indices) {
        for (j in array[i].indices) {
            if (array[i][j] < 0) {
                sum += -array[i][j]
            }
        }
    }

    println("Сумма модулей отрицательных элементов: $sum")
}