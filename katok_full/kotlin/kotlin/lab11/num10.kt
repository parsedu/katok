package lab11

fun main() {

    val array = arrayOf(1, 3, 5, 7, 9, 11, 6, 8, 12)
    //val array = arrayOf(12, 11, 10, 9, 8, 7, 6, 5)

    var ord = true
    var ind = -1

    for (i in 0 until array.size - 1) {
        if (array[i] < array[i + 1]) {
            ord = false
            ind = i
            break
        }
    }

    if (ord) {
        println("Массив упорядочен по убыванию")
        array[0] = array[0] * array[0]
        array[array.size - 1] = array[array.size - 1] * array[array.size - 1]
        println("Первый и последний элементы возведены в квадрат")
    } else {
        println("Массив НЕ упорядочен по убыванию")
        println("Нарушение порядка на индексе: $ind")
        if (ind < array.size - 1) {
            val temp = array[ind]
            array[ind] = array[ind + 1]
            array[ind + 1] = temp
            println("Элемент $ind поменян с элементом ${ind + 1}")
        }
    }

    println("Массив №2: ")
    for (num in array) {
        print("$num ")
    }
}