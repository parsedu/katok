package lab11

fun main() {
    val array = arrayOf(3, 7, 2, 8, 1, 9, 4, 6)


    var maxin = 0
    var minin = 0
    var maxval = array[0]
    var minval = array[0]

    for (i in 1 until array.size) {
        if (array[i] > maxval) {
            maxval = array[i]
            maxin = i
        }
        if (array[i] < minval) {
            minval = array[i]
            maxin = i
        }
    }

    println("Максимальный элемент: $maxval (индекс $maxin)")
    println("Минимальный элемент: $minval (индекс $minin)")

    if (maxin < minin) {
        array[0] = minval
        println("Максимальный элемент встречается раньше")
        println("Заменили первый элемент на минимальный: $minval")
    } else {
        array[array.size - 1] = maxval

    }

    println("Массив №2: ")
    for (num in array) {
        print("$num ")
}}