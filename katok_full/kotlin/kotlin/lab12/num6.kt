package lab12

fun main() {
    val array = arrayOf(
        arrayOf(5, -3, 8),
        arrayOf(-1, 0, -7),
        arrayOf(2, -4, 6)
    )


    var product = 1

    for (i in array.indices) {
        for (j in array[i].indices) {
            val mod = if (array[i][j] < 0) -array[i][j] else array[i][j]
            if (mod in 1..5) {
                product *= array[i][j]
            }
        }
    }

    println("Произведение элементов, чей модуль лежит в диапазоне [1; 5]: $product")
}