package lab16

fun randomBukva(size: Int): CharArray {
    val res = CharArray(size)
    val random = java.util.Random()

    for (i in 0 until size) {
        val ranBukva = ('A'.code + random.nextInt(26)).toChar()
        res[i] = ranBukva
    }

    return res
}

fun main() {
    println("Введите размер массива:")
    val size = readln().toInt()
    val letters = randomBukva(size)
    println("\nМассив:")
    println(letters.joinToString(" ", "[", "]"))
}