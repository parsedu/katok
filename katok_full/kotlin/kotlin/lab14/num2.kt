package lab14

fun main(){
val array = arrayOf(
    arrayOf(1, 2, 3),
    arrayOf(4, 5, -10),
    arrayOf(7, 0, 9)
)
var maxE = array[0][0]
var maxER = 0
var maxEC = 0

for (i in array.indices) {
    for (j in array[0].indices) {
        if (array[i][j] > maxE) {
            maxE = array[i][j]
            maxER = i
            maxEC = j
        }
    }
}

println("Максимальный элемент: $maxE (индекс: [$maxER, $maxEC])")

    array[maxER][maxEC] *= 2

val lastRow = array.last()
val minLastRow = lastRow.minOrNull() ?: 0

println("Минимальный элемент последней строки: $minLastRow")

for (i in array.indices) {
    for (j in array[0].indices) {
        if (i != maxER || j != maxEC) {
            array[i][j] -= minLastRow
        }
    }
}

println("Массив B после изменений:")
    array.forEach { row -> println(row.contentToString()) }
}

