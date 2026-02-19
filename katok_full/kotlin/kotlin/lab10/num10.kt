package lab10

fun main() {
    val numbers = arrayOf(11, -22, -33, 44, 55, -66,-77, 88, -99, 10)
    print("Массив №1: ")
    for (num in numbers) {
        print("$num ")
    }
    println()
    var count = 0
    for (i in numbers.indices) {
        if (numbers[i] < 0){
            numbers[i] = numbers[i] / 3

        }
    }
    print("Массив№2: ")
    for (num in numbers) {
        print("$num ")
    }
    println()
}