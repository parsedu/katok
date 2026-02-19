package lab16

fun removeChtotamArray(arr: Array<Int>): Array<Int> {
    if (arr.isEmpty()) return emptyArray()
    var count = 0
    val temp = IntArray(arr.size)

    for (i in arr.indices) {
        var Dupl = false

        for (j in 0 until count) {
            if (arr[i] == temp[j]) {
                Dupl = true
                break
            }
        }
        if (!Dupl) {
            temp[count] = arr[i]
            count++
        }
    }
    val result = IntArray(count)
    for (i in 0 until count) {
        result[i] = temp[i]
    }

    return result.toTypedArray()
}
fun main() {
    val arra = arrayOf(1, 2, 2, 3, 4, 4, 5)

    println("Числа: ${removeChtotamArray(arra).joinToString()}")
}