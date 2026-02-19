package lab12

fun main() {
    val array = arrayOf(
        arrayOf(5, -3, 8),
        arrayOf(-1, 0, -7),
        arrayOf(2, -4, 6)
    )

    var sum = 0
    var count = 0

    for (i in array.indices) {
        for (j in array[i].indices) {
            if (array[i][j] % 4 == 1 || array[i][j] % 4 == 3) {
                sum += array[i][j]
                count++
            }
        }
    }

    if (count > 0) {
        val avg = sum.toDouble() / count
        println("Среднее арифметическое элементов, которые при делении на 4 дают остаток 1 или 3: $avg")
    } else {
        println("Подходящих элементов нет")
    }
}