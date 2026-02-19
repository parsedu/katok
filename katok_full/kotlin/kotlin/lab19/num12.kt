package lab19

fun main() {
    println("Введите строку:")
    val input = readln()

    val words = input.split(" ")
    val res = mutableListOf<String>()

    for (word in words) {
        if (word.isEmpty()) {
            res.add("")
        } else if (word.length == 1) {
            res.add(word.uppercase())
        } else {
            val lastIndex = word.length - 1
            val newWord = word.substring(0, lastIndex) + word[lastIndex].uppercaseChar()
            res.add(newWord)
        }
    }

    val result = res.joinToString(" ")

    println("Стало: \"$result\"")
}