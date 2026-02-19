
fun main() {
    var t = 0
    val numbers = arrayOf(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    for (num in numbers) {
        if (num < -1 || num > 5) {
            t += num
        }
        numbers.forEach { num ->
            println(num)
        }
        println(t)
    }
}


