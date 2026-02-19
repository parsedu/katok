package lab19

fun main() {
    println("Введите строку:")
    val input = readln()

    var cifr = true

    for (char in input) {
        if (!char.isDigit()) {
            cifr = false
            break
        }
    }

    println("$cifr")
}