package lab12

fun main() {
    val array = arrayOf(
        arrayOf(5, -3, 8),
        arrayOf(-1, 0, -7),
        arrayOf(2, -4, 6)
    )

    var product = 1.0
    var count = 0

    for (i in array.indices) {
        for (j in array[i].indices) {
            if (array[i][j] < 0) {
                product *= -array[i][j]
                count++
            }
        }
    }

    if (count > 0) {
        val avg = Math.pow(product, 1.0 / count)
        println("Среднее геометрическое модулей отрицательных элементов: $avg")
    } else {
        println("Отрицательных элементов нет")
    }
}