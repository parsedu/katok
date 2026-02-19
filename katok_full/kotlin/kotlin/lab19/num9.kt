package lab19

fun main() {
    println("Введите строку:")
    val input = readln()
    val res = input.replace(" ", "-")
    println("\nРезультат:")
    println(res)
}