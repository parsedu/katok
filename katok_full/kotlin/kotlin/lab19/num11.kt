package lab19

fun main() {
    println("Введите текст:")
    val text = readln()

    print("Введите букву для поиска: ")
    val letter = readln().lowercase()

    val words = text.split(" ").filter { it.isNotBlank() }
    val result = words.filter { it.lowercase().startsWith(letter) }

    println("\nСлова, начинающиеся на '$letter':")
    if (result.isEmpty()) {
        println("Не найдено")
    } else {
        result.forEachIndexed { index, word ->
            println("${index + 1}. $word")
        }
    }
}