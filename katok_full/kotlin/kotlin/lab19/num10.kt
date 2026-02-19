package lab19

fun main() {
    println("Введите предложение:")
    val inp = readln()
    val words = inp.trim().split("\\s+".toRegex())

    for (i in words.indices) {
        println("  Слово[$i] = \"${words[i]}")
    }
}