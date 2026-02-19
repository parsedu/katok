package lab10

fun main() {
    val numbers = arrayOf(14, 12, -33, 64, 665, -216, -7, -8, -9, 10)
    print("Массив №1: ")
    for (num in numbers) {
        print("$num ")
    }
    println()
    var count = 0
    for (i in numbers.indices) {
        if (numbers[i] < 0) {
            count++
            if (count % 2 == 0){
                numbers[i] = numbers[i] * numbers[i]
            }
        }
    }
    print("Массив№2: ")
    for (num in numbers) {
        print("$num ")
    }
    println()
}