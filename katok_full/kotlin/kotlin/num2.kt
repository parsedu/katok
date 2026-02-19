import kotlin.math.*

fun main() {
    println("Вариант №5")
    println("№1:")
    print("Введите k: ")
    val k = readLine()?.toDouble() ?: 0.0
    print("Введите b: ")
    val b = readLine()?.toDouble() ?: 0.0
    print("Введите R: ")
    val R = readLine()?.toDouble() ?: 0.0
    val A = 1 + k * k
    val B = 2 * k * b
    val C = b * b - R * R

    val dis = B * B - 4 * A * C

    val ip = when {
        dis < 0 -> 0
        abs(dis) < 1e-10 -> 1
        else -> 2
    }

    println("Число точек пересечения: $ip")
    println("------------------------------------------------------")

    println("№ 2:")
    print("Введите k: ")
    val k2 = readLine()?.toInt() ?: 0
    print("Введите l: ")
    val l2 = readLine()?.toInt() ?: 0

    var resultK = k2
    var resultL = l2

    if (k2 != l2) {
        val maxValue = max(k2, l2)
        resultK = maxValue
        resultL = maxValue
    } else {
        if (k2 < 0) {
            resultK = k2 * k2
            resultL = l2 * l2
        } else {
            resultK = k2 * 2
            resultL = l2 * 2
        }
    }

    println("Результат: k = $resultK, l = $resultL")
    println("------------------------------------------------------")

    println("№ 3:")
    print("Введите a: ")
    val a = readLine()?.toInt() ?: 0
    print("Введите b: ")
    val bb = readLine()?.toInt() ?: 0
    print("Введите c: ")
    val c = readLine()?.toInt() ?: 0

    var resultA = a
    var resultB = bb
    var resultC = c

    if (a % 3 == 0 && bb % 3 == 0 && c % 3 == 0) {
        val sum = a + bb + c
        println("Сумма чисел: $sum")
    } else {
        if (a % 2 == 0) resultA = a * 3
        if (bb % 2 == 0) resultB = bb * 3
        if (c % 2 == 0) resultC = c * 3
        println("Результат: a = $resultA, b = $resultB, c = $resultC")
    }

    println("------------------------------------------------------")

    println("№ 5:")
    print("Введите число A: ")
    val a5 = readLine()?.toDouble() ?: 0.0
    print("Введите число B: ")
    val b5 = readLine()?.toDouble() ?: 0.0
    print("Введите число C: ")
    val c5 = readLine()?.toDouble() ?: 0.0

    var poloz = 0
    var oterc = 0

    if (a5 > 0) poloz++ else if (a5 < 0) oterc++
    if (b5 > 0) poloz++ else if (b5 < 0) oterc++
    if (c5 > 0) poloz++ else if (c5 < 0) oterc++

    println("Положительных чисел: $poloz")
    println("Отрицательных чисел: $oterc")
    println("------------------------------------------------------")


    println("№ 6:")
    print("Введите число A: ")
    val a6 = readLine()?.toDouble() ?: 0.0
    print("Введите число B: ")
    val b6 = readLine()?.toDouble() ?: 0.0
    print("Введите число C: ")
    val c6 = readLine()?.toDouble() ?: 0.0

    println("Пары чисел одного знака:")

    if ((a6 > 0 && b6 > 0) || (a6 < 0 && b6 < 0)) println("A и B: ($a6, $b6)")
    if ((a6 > 0 && c6 > 0) || (a6 < 0 && c6 < 0)) println("A и C: ($a6, $c6)")
    if ((b6 > 0 && c6 > 0) || (b6 < 0 && c6 < 0)) println("B и C: ($b6, $c6)")
    println("------------------------------------------------------")


    println("№ 7:")
    print("Введите часы (C): ")
    var chas  = readLine()?.toInt() ?: 0
    print("Введите минуты (M): ")
    var minut = readLine()?.toInt() ?: 0
    print("Введите секунды (S): ")
    var sec = readLine()?.toInt() ?: 0

    sec += 15

    if (sec >= 60) {
        minut += sec / 60
        sec %= 60
    }

    if (minut >= 60) {
        chas += minut / 60
        minut %= 60
    }

    if (chas >= 24) {
        chas %= 24
    }

    println("Время через 15 секунд: ${String.format("%02d:%02d:%02d", chas, minut, sec)}")
    println("------------------------------------------------------")


   println("№ 8:")
   print("Введите число A: ")
   val a8 = readLine()?.toDouble() ?: 0.0
   print("Введите число B: ")
   val b8 = readLine()?.toDouble() ?: 0.0
   print("Введите число C: ")
   val c8 = readLine()?.toDouble() ?: 0.0
        val middle = when {
        (a8 >= b8 && a8 <= c8) || (a8 <= b8 && a8 >= c8) -> a8
        (b8 >= a8 && b8 <= c8) || (b8 <= a8 && b8 >= c8) -> b8
        else -> c8
        }

    println("Среднее число: $middle")
    println("------------------------------------------------------")

    println("№ 9:")
    print("Введите высоту h (0 < h < 46000): ")
    val h = readLine()?.toDouble() ?: 0.0

    val temp = when {
        h < 11000 -> 288.16 - 0.0065 * h
        h <= 25000 -> 216.16
        else -> 216.16 + 0.00276098 * (h - 25000)
    }

    println("Температура на высоте ${"%.2f".format(h)} м: ${"%.2f".format(temp)} K")
    println("------------------------------------------------------")


    println("№ 10:")
    print("Введите x вектора A: ")
    val xa = readLine()?.toDouble() ?: 0.0
    print("Введите y вектора A: ")
    val ya = readLine()?.toDouble() ?: 0.0
    print("Введите z вектора A: ")
    val za = readLine()?.toDouble() ?: 0.0

    print("Введите x вектора B: ")
    val xb = readLine()?.toDouble() ?: 0.0
    print("Введите y вектора B: ")
    val yb = readLine()?.toDouble() ?: 0.0
    print("Введите z вектора B: ")
    val zb = readLine()?.toDouble() ?: 0.0


    val modA = sqrt(xa * xa + ya * ya + za * za)
    val modB = sqrt(xb * xb + yb * yb + zb * zb)

    println("Модуль вектора A: ${"%.2f".format(modA)}")
    println("Модуль вектора B: ${"%.2f".format(modB)}")

    if (modA > modB) {
        val sPr = xa * xb + ya * yb + za * zb
        println("Скалярное произведение S = $sPr")
    } else {
        val r = sqrt(abs(modB - modA))
        println("R = sqrt(|B| - |A|) = ${"%.2f".format(r)}")
    }
}

