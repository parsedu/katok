import kotlin.math.*

fun main() {
    print("k = : ")
    val k = readLine()?.toInt() ?: 1
    print("x = : ")
    val x = readLine()?.toDouble() ?: 1.0

    var n = 1
    var sum = 0.0

    while (n <= k) {
        val num = 2 + n * n * n
        val d= sqrt(x * x + n * n)
        sum += num / d
        n++
        println("S = $sum")
    }
}