fun main() {
    var t = 1
    val numbers = arrayOf(1,2,3,4,5,6,7,8,9,10,11,12)
    var i = 0

    while (i < numbers.size) {
        if (numbers[i] % 2 == 0) {
            t *= numbers[i]
        }
        i++
    }
    println(t)
}