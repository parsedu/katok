package lab9
fun main() {
    val x1 = 0.0
    val y1 = 0.0
    val x2 = 0.0
    val y2 = 5.0
    val x3 = 3.0
    val y3 = 0.0
    val x4 = if (x1 == x2) x3 else if (x1 == x3) x2 else x1
    val y4 = if (y1 == y2) y3 else if (y1 == y3) y2 else y1

    println("Координаты четвертой вершины: ($x4, $y4)")
}