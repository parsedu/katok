package lab19

fun LsCh(input: String): Char {
    return input.last()
}

fun main() {
    print("Введите строку: ")
    val usInp = readlnOrNull() ?: ""
    if (usInp.isNotEmpty()) {
        val lastChar = LsCh(usInp)
        println("Последний символ: $lastChar")
    }
}