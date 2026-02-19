package lab16

fun secVDay(seconds: Long): Long {
    var day = 0L
    var s = seconds
    while (s >= 86400) {
        s -= 86400
        day++
    }

    return day
}

fun main() {
    val vvod = listOf(50000L, 86400L, 100000L, 86400L * 3, 86400L * 10 + 5000L)
    for (sec in vvod) {
        val days = secVDay(sec)
        val ream = sec - days * 86400
        println("$sec сек = $days суток (остаток: $ream сек)")
    }
}