import kotlin.math.*

fun main() {
    println("№6:")
    print("Введите k: ")
    val k6 = readLine()?.toInt() ?: 1

    var x = -1.5
    val dx = 0.4
    val endX = 5.0

    println("x\t\tf(x)\t\tделение на 2\tделение на 3")
    println("---------------------------------------------------")

    while (x <= endX + 0.001) {
        val fx = 2.0.pow(k6) * (x * x + x - 1)
        val intFx = fx.toInt()
        val mod2 = intFx % 2
        val mod3 = intFx % 3


        println("%.1f\t\t%.2f\t\t%d\t\t\t%d".format(x, fx, mod2, mod3))
        x += dx
    }
    println("------------------------------------------------------------------------")


    println("№ 7:")
    var x7 = -3.0
    val dx7 = 0.35
    val endX7 = 3.0
    val th = 1.0 / sqrt(3.0)

    println("x\t\tf(x)\t\t|cos(x)|")
    println("------------------------------------------------")

    do {
        val cosX = abs(cos(x7))
        val fx = if (cosX > th) {
            sqrt(1.0 / sqrt(3.0) + x7 * x7)
        } else {
            sqrt(1.0 / sqrt(3.0) - cosX)
        }

        println("%.2f\t\t%.4f\t\t%.4f".format(x7, fx, cosX))
        x7 += dx7
    } while (x7 <= endX7 + 0.001)
    println("------------------------------------------------------------------------")


    println("№9:")
    print("Введите a: ")
    val a9 = readLine()?.toInt() ?: 0

    val startK9 = -10
    val endK9 = 10
    val dk9 = 1

    println("k\t\tf(k)\t\tТип числа")
    println("----------------------------")

    for (k in startK9..endK9 step dk9) {
        val fk = if (k % 2 == 0) {
            a9 + 12 / k
        } else {
            k * k
        }

        val type = if (k % 2 == 0) "четное" else "нечетное"
        println("$k\t\t$fk\t\t$type")
    }
    println("------------------------------------------------------------------------")

}

