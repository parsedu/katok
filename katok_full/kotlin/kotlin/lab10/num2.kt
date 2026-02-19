package lab10

fun main() {
    val numbers = arrayOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    print("мМассив №1: ")
    for (num in numbers) {
        print("$num ")
    }
    println()

    for (i in numbers.indices) {
        if (numbers[i] % 2 == 0) {
            numbers[i] /= 2
        }
    }
    print("Массив №2: ")
    for (num in numbers) {
        print("$num ")
    }
    println()
}