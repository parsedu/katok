import java.lang.Math.sin
import java.lang.Math.tan
import java.sql.DriverManager.println

fun main() {
    val a1 = 0.5
    val y1 = 1.2
    var x1 = tan(y1).toInt()
    println("Исход х: $x1")

    if (sin(x1 + a1.toDouble()) == 0.0) {
        x1 *= 3
        println("Выражение равно нулю, х утроен: $x1")
    } else {
        println("Выражение  не равно нулю, x прежд:$x1")
    }
}
