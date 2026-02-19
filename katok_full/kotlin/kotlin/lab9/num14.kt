package lab9

fun main() {
    val text = "ffffffffffffffffffffffffffffffffffffffff"

    println("1. по левому краю:")
    println(text)
    println()

    println("2. по правому краю:")
    println("%100s".format(text))
    println()

    println("3. по центру:")
    val centered = text.padStart((100 + text.length) / 2).padEnd(100)
    println(centered)
    println()

    println("4. по ширине:")
    println(text)
}