fun main() {
    val text = "Hello World и Kotlin!"

    val buk = setOf('a', 'e', 'i', 'o', 'u', 'y', 'а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я')

    var gl = 0
    var cog = 0

    for (char in text.lowercase()) {
        if (char.isLetter()) {
            if (char in buk) {
                gl++
            } else {
                cog++
            }
        }
    }

    println("Гласные: $gl")
    println("Согласные: $cog")
}