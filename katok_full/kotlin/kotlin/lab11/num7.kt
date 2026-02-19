package lab11


fun main() {
    val numbers = arrayOf(10, 2, 3, 4, 5, 6,7, 8, 9, 10)
    println("Массив №1: ")
    for (num in numbers) {
        print("$num ")
    }
    println()
    var count = 1
    var count_min = 1
    var count_min2 = 1
    var max = numbers.max()
    var min = numbers.min()
    for(i in numbers.indices){
        if (numbers[i] %2 == 0){
            count++
        }
    }


    if (min > 0) {
        for (i in 0 until min) {
            count_min *= numbers[i]
            println(count)
        }
    }
    if (min < numbers.size - 1) {
        for (i in min + 1 until numbers.size) {
            count_min2 *= numbers[i]
            println(count)
        }
    }
    println(count)

    println("Массив №2: ")
    for (num in numbers) {
        print("$num ")

    }

}

