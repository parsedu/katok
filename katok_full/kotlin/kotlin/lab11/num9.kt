package lab11

fun main() {

    //val array = arrayOf(1, 3, 5, 7, 9, 11, 6, 8, 12)
    val array = arrayOf(1, 2, 3, 4, 5, 6, 7, 8, 12)
    var ord = true
    for (i in 0 until array.size - 1) {
        if (array[i] > array[i + 1]) {
            ord = false
            break
        }
    }

    if (ord) {
        println("Массив упорядочен по возрастанию")

        for (i in array.indices) {
            array[i] = array[i] * array[i]
        }
        println("Все элементы возведены в квадрат")
    } else {
        println("Массив НЕ упорядочен по возрастанию")

        val temp = array[0]
        array[0] = array[array.size - 1]
        array[array.size - 1] = temp
        println("Первый и последний элементы поменяны местами")
    }

    println("Массив №2: ")
    for (num in array) {
        print("$num ")
    }
}