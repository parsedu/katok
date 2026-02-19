package lab14


fun main() {

    val array = arrayOf(
        arrayOf(2, 5, 1, 8),
        arrayOf(4, 3, 7, 6),
        arrayOf(9, 0, 2, 5)
    )
    val n = 3
    val m = 4

    var minValue = array[0][0]
    var minColumn = 0

    for (i in 0 until n) {
        for (j in 0 until m) {
            if (array[i][j] < minValue) {
                minValue = array[i][j]
                minColumn = j
            }
        }
    }

    var product = 1
    for (i in 0 until n) {
        product *= array[i][minColumn]
    }

    for (i in 0 until n) {
        for (j in 0 until m) {
            array[i][j] += product
        }
    }

    println("Массив после преобразования (столбец с минимальным элементом: ${minColumn + 1}, произведение: $product):")
    for (i in array.indices) {
        for (j in array[i].indices) {
            print("${array[i][j]}\t")
        }
        println()
    }
}
