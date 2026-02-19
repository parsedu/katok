package lab12

fun main() {
    val array = arrayOf(
        arrayOf(5, -3, 8),
        arrayOf(-1, 0, -7),
        arrayOf(2, -4, 6)
    )



    var prod = 1.0
    var count = 0

    for (i in array.indices) {
        for (j in array[i].indices) {
            if (array[i][j] < 0) {
                val square = array[i][j] * array[i][j]
                prod *= square
                count++
            }
        }
    }

    if (count > 0) {
        val avg = Math.pow(prod, 1.0 / count)
        println("Среднее геометрическое квадратов отрицательных элементов: $avg")
    } else {
        println("Отрицательных элементов нет")
    }
}