package lab16

fun remArr(arr: IntArray): IntArray {
    if (arr.isEmpty()) return intArrayOf()

    val result = mutableListOf<Int>()
    result.add(arr[0])

    for (i in 1 until arr.size) {
        if (arr[i] != arr[i - 1]) {
            result.add(arr[i])
        }
    }

    return result.toIntArray()
}
fun main() {
    val input1 = intArrayOf(1, 2, 2, 3, 4, 4, 4, 5, 5, 6)
    val output1 = remArr(input1)
    println(output1.joinToString(", "))

}