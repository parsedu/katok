package lab19

fun main() {
    println("Введите строку:")
    val input = readln()

    print("N= ")
    val n = readln().toIntOrNull() ?: 1

    val words = input.split(" ").filter { it.isNotBlank() }
    val fword = words.take(n)

    val result = fword.joinToString(" ")

    println("\nПервые $n слов:")
    println(result)
}