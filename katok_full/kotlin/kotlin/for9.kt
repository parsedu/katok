import kotlin.math.sqrt
fun main() {
    print("k =: ")
    val k = readLine()?.toInt() ?: 1

    var p = 1.0
    for (n in 100 downTo k step 2) {
        val num = n.toDouble()
        val d = 1 + sqrt(n * n * n.toDouble())
        p *= num / d
        println("P = $p")
    }
    println()
}