package lab19

fun main() {
    print("Введите строку: ")
    val text = readln()

    print("Введите подстроку: ")
    val text2 = readln()

    println(" ${text2 in text}")
}