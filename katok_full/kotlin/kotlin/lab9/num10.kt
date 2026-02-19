package lab9
fun main() {
    val sentence = "Мое короткое предложение"

    println("Количество символов: ${sentence.length}")
    val words = sentence.split(" ")

    println("Количество слов: ${words.size}")

    var shor = words[0]
    var long = words[0]

    for (word in words) {
        if (word.length < shor.length) shor = word
        if (word.length > long.length) long = word
    }

    println("Самое короткое слово: '$shor'")
    println("Самое длинное слово: '$long'")
}