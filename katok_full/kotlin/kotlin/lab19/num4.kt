package lab19

fun main() {
    print("Введите строку: ")
    val text = readln()

    print("Введите подстроку: ")
    val text2 = readln()

    val result = text.startsWith(text2)
    println("$result")
}