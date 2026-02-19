package lab14

fun main() {

    val array = arrayOf(
        intArrayOf(4, -2, 5),
        intArrayOf(1, -6, 3),
        intArrayOf(-8, 7, 9)
    )

    println("Исходный массив:")
    printArray(array)

    var maxRowIndex = 0
    var maxElement = array[0][0]
    var minRowIndex = 0
    var minElement = array[0][0]

    for (i in array.indices) {
        for (j in array[i].indices) {
            if (array[i][j] > maxElement) {
                maxElement = array[i][j]
                maxRowIndex = i
            }
            if (array[i][j] < minElement) {
                minElement = array[i][j]
                minRowIndex = i
            }
        }
    }

    println("\nМаксимальный элемент: $maxElement (строка $maxRowIndex)")
    println("Минимальный элемент: $minElement (строка $minRowIndex)")

    if (maxRowIndex == minRowIndex) {
        for (j in array[maxRowIndex].indices) {
            array[maxRowIndex][j] = if (j == maxRowIndex) 1 else 0
        }
        println("\nСтрока с максимумом и минимумом совпадает.")
        printArray(array)
    } else {
        val tempRow = array[maxRowIndex].copyOf()
        array[maxRowIndex] = array[minRowIndex].copyOf()
        array[minRowIndex] = tempRow

        println("\nМеняем местами строку $maxRowIndex и строку $minRowIndex:")
        printArray(array)
    }
}

