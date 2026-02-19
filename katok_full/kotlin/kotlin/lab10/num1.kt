package lab10
fun main() {
    val numbers = arrayOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print("Масив №1: ")
    for (num in numbers) {
        print("$num ")
    }
    println()

    for (i in numbers.indices) {
        if ((i + 1) % 3 == 0) {
            numbers[i] *= i
        }
    }
    print("Массив №2: ")
    for (num in numbers) {
        print("$num ")
    }
    println()
}