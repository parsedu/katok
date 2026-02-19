package lab16

fun minMax(arr: IntArray): IntArray {
    if (arr.isEmpty()) return intArrayOf()

    var min = arr[0]
    var max = arr[0]

    for (i in 1 until arr.size) {
        if (arr[i] < min) min = arr[i]
        if (arr[i] > max) max = arr[i]
    }

    return intArrayOf(max, min)
}

fun main() {
    val testArrays = arrayOf(
        intArrayOf(5, 3, 8, 1, 9, 2),
        intArrayOf(10, 10, 10, 10),
        intArrayOf(-5, -1, -8, -3),
        intArrayOf(0, 100, -50, 25)
    )

    for (arr in testArrays) {
        val result = minMax(arr)
        println("${result[0]}, ${result[1]}")
    }
}