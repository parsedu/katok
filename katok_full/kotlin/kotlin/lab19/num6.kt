package lab19

fun PoiskPoz() {
    val text = readln()
    val text2 = readln()
    val pos = text.indexOf(text2)
    println(if (pos >= 0) "Позиция: $pos" else "Не найдено")
}

fun main() {
    PoiskPoz()
}