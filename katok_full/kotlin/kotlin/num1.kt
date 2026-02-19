import java.sql.DriverManager
import kotlin.math.*
fun main() {
    println(" №1")
    val a1 = 0.5
    val y1 = 1.2
    var x1 = tan(y1).toInt()
    println("Исходное x: $x1")

    if (sin(x1 + a1.toDouble()) == 0.0) {
        x1 *= 3
        println("Выражение обращается в ноль, x утроен: $x1")
    } else {
        println("Выражение не обращается в ноль x остался: $x1")
    }
    println("-------------------------------------------------")

    println("№2")
    val m2 = 7
    val n2 = 3
    val k2 = 5

    val frc = m2.toDouble() / n2
    val frc2 = n2.toDouble() / k2
    val frp1 = frc - frc.toInt()
    val frp2 = frc2 - frc2.toInt()

    if (abs(frp1 - frp2) < 1e-10) {
        println("Дробные части равны: $frc и $frc2")
    } else {
        println("Дробные части не равны")
    }
    println("-------------------------------------------------")

    println("№3")
    val m3 = 5
    val n3 = 2
    val k3 = 3

    val fr3_1 = m3.toDouble() / n3
    val fr3_2 = n3.toDouble() / k3
    val frP3_1 = fr3_1 - fr3_1.toInt()
    val frP3_2 = fr3_2 - fr3_2.toInt()

    if (abs(frP3_1 - frP3_2) < 1e-10) {
        println("Дробные части равны: ${"%.4f".format(frP3_2)}")
    } else {
        println("Дробные части: ${"%.4f".format(frP3_1)} и ${"%.4f".format(frP3_2)}")
    }
    println("-------------------------------------------------")

    println("№4")
    var m4 = 7
    var n4 = 3

    val fr4 = m4.toDouble() / n4
    val frP4 = fr4 - fr4.toInt()
    println("Дробная часть: ${"%.4f".format(frP4)}")

    if (frP4 > 0.5) {
        m4 *= 3
        println("Дробная часть > 0.5, m утроен: $m4")
    } else {
        n4 *= 3
        println("Дробная часть <= 0.5, n утроен: $n4")
    }
    println("-------------------------------------------------")

    println("№5")
    val m5 = 17
    val n5 = 4

    val fr5 = m5.toDouble() / n5
    val iP5 = fr5.toInt()
    val frP5 = fr5 - iP5
    val mF = frP5 * 10

    println("Целая часть: $iP5, дробная часть * 10: ${"%.2f".format(mF)}")

    if (mF > iP5) {
        val dif = mF - iP5
        println("Превышает на: ${"%.2f".format(dif)}")
    } else {
        println("Не превышает")
    }
    println("-------------------------------------------------")

    println("№6")
    var m6 = 11
    var n6 = 4

    val fraction6 = m6.toDouble() / n6
    val intPart6 = fraction6.toInt()

    if (intPart6 % 2 == 0) {
        m6 = m6 * m6
        println("Целая часть четная, m возведен в квадрат: $m6")
    } else {
        n6 *= 3
        println("Целая часть нечетная, n утроен: $n6")
    }
    println("-------------------------------------------------")

    println("№7")
    val m7 = 23
    val n7 = 5

    val fr7 = m7.toDouble() / n7
    val iP7 = fr7.toInt()
    val k7 = m7 % 5

    println("Целая часть: $iP7, остаток от деления m на 5: $k7")

    if (iP7 > k7) {
        val sq = fr7 * fr7
        println("Целая часть > k, дробь в квадрате: ${"%.4f".format(sq)}")
    } else {
        println("Условие не выполнено")
    }
    println("-------------------------------------------------")

    println("№8")
    val m8 = 17
    val n8 = 5

    val fr8 = m8.toDouble() / n8
    val iP8 = fr8.toInt()
    val k8 = m8 % 5

    println("Целая часть: $iP8, остаток от деления m на 5: $k8")

    if (iP8 == k8) {
        println("Целая часть равна остатку от деления")
    } else {
        println("Целая часть не равна остатку от деления")
    }
    println("-------------------------------------------------")

    println("№9")
    val m9 = 17
    val n9 = 5

    val fr9 = m9.toDouble() / n9
    val frP9 = fr9 - fr9.toInt()
    val k9 = m9 % 5

    println("Дробная часть: ${"%.4f".format(frP9)}, остаток от деления m на 5: $k9")

    if (abs(frP9 - k9) < 1e-10) {
        println("Дробная часть равна остатку от деления")
    } else {
        println("Дробная часть не равна остатку от деления")
    }
    println("-------------------------------------------------")

    println("№10")
    val m10 = 17
    val n10 = 5

    val fr10 = m10.toDouble() / n10
    val fP10 = fr10 - fr10.toInt()
    val k10 = m10 % 5

    println("Дробная часть: ${"%.4f".format(fP10)}, остаток от деления m на 5: $k10")

    if (abs(fP10 - k10) < 0.1) {
        println("Дробная часть равна остатку от деления с точностью 0.1")
    } else {
        println("Дробная часть не равна остатку от деления с точностью 0.1")
    }
}

