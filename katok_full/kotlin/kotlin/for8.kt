import kotlin.math.*

fun main() {
    print("k = : ")
    val k = readLine()?.toInt() ?: 1

    var sum = 0.0
    for (n in 1..k) {
        val num = 1 + sqrt(n * n * n.toDouble())
        val d = sqrt(1 + n * n.toDouble())
        sum += num / d
        println("S = $sum")
    }
    println()
}

