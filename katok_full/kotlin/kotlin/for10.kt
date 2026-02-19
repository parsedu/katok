import kotlin.math.exp
fun main() {
print("k =: ")
val k = readLine()?.toInt() ?: 1

var sum = 0.0
for (n in 1..k) {
    val num = exp(n.toDouble())
    val d = n * n * n.toDouble()
    sum += num / d
    println("S = $sum")
}
}
