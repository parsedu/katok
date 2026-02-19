package lab19

fun main() {
    val stArray = arrayOf("Cat", "Dog", "Java")
    var total = 0
    for (str in stArray) {
        total += str.length
    }
    val chArr = CharArray(total)
    var index = 0

    for (str in stArray) {
        for (char in str) {
            chArr[index] = char
            index++
        }
    }

    println("Строки: ${stArray.joinToString()}")
    println("Все символы: ${chArr.joinToString()}")
}