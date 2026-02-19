package lab12

fun main() {
    val array = arrayOf(
        arrayOf(5, -3, 8),
        arrayOf(-1, 0, -7),
        arrayOf(2, -4, 6)
    )


    var prod = 1

    for (i in array.indices) {
        for (j in array[i].indices) {
            val modulus = if (array[i][j] < 0) -array[i][j] else array[i][j]
            if (modulus < 1 || modulus > 5) {
                prod *= array[i][j]
            }
        }
    }

    println("Произведение элементов, чей модуль лежит вне диапазона [1; 5]: $prod")
}