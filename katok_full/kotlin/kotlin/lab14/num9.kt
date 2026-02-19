package lab14
fun main() {
    val array = arrayOf(
        arrayOf(4, -2, 5),
        arrayOf(1, -6, 3),
        arrayOf(-8, 7, 9)
    )



    val dlEle = mutableListOf<Int>()

    for (i in array.indices) {
        dlEle.add(array[i][i])
        val j = array.size - 1 - i
        if (i != j) {
            dlEle.add(array[i][j])
        }
    }

    val average = dlEle.average()
    println("\nСреднее арифметическое диагональных элементов: $average")
    println("Диагональные элементы: ${dlEle.joinToString()}")

    val multiples = if (average != 0.0) {
        array.flatMap { row ->
            row.filter { element ->

                if (average.toInt().toDouble() == average) {
                    val intAvg = average.toInt()
                    intAvg != 0 && element % intAvg == 0
                } else {
                    false
                }
            }
        }
    } else {
        emptyList()
    }

    println("Элементы, кратные среднему арифметическому: ${
        if (multiples.isNotEmpty()) multiples.joinToString()
        else if (average == 0.0) "нет (среднее = 0)"
        else "нет (среднее не целое число)"
    }")

    val minValue = array.flatMap { it.toList() }.minOrNull() ?: 0
    val smallerThanMin = array.flatMap { row ->
        row.filter { it < minValue }
    }
    println("\nМинимальное значение в массиве: $minValue")
    println("Элементы, меньше мин.знач: ${smallerThanMin.joinToString()}")


    val sqArray = Array(array.size) { i ->
        IntArray(array[i].size) { j ->
            if (i + j > array.size - 1) {
                array[i][j] * array[i][j]
            } else {
                array[i][j]
            }
        }
    }

    println("\nМассив после возведения в квадрат элементов под побочной диагональю:")
    printArray(sqArray)

    val fArray = Array(sqArray.size) { i ->
        IntArray(sqArray[i].size) { j ->
            if (i > j) {
                sqArray[i][j] + minValue
            } else {
                sqArray[i][j]
            }
        }
    }

    println("\nИтоговый массив:")
    printArray(fArray)
}

fun printArray(array: Array<IntArray>) {
    for (row in array) {
        println(row.joinToString("\t"))
    }
}