import kotlin.math.sqrt

fun main() {

var p = 1.0
var n = 1

do {
    val num = 2 + n
    val d = 2 + sqrt(n * n * n.toDouble())
    p *= num / d
    n++
    println("P = $p")
} while (n <= 5)


}