package lab14

fun main() {
    val array = arrayOf(
        arrayOf(-1, 2, 3),
        arrayOf(4, -5, 6),
        arrayOf(7, -8, 9)
    )
        var minAbs = Math.abs(array[0][0])
        var maxAbs = Math.abs(array[0][0])

    for (i in array.indices) {
        for (j in array[i].indices) {
                val absVal = Math.abs(array[i][j])
                if (absVal < minAbs) minAbs = absVal
                if (absVal > maxAbs) maxAbs = absVal
            }
        }

        val th = (minAbs + maxAbs) / 2
        var count = 0


    for (i in array.indices) {
        for (j in array[i].indices) {
                val absVal = Math.abs(array[i][j])
                if (absVal > 0 && absVal < th) {
                    array[i][j] *= array[i][j]
                    count++
                }
            }
        }

        println("\nМассив после преобразования:")
    for (i in array.indices) {
        for (j in array[i].indices) {
                print("${array[i][j]}\t")
            }
            println()
        }

        println("\nКоличество элементов, возведенных в квадрат: $count")
}
