package lab19

fun main() {
    println("Введите текст:")
    val input = readln()
    val sen = mutableListOf<String>()
    var Ssq = 0

    for (i in input.indices) {
        val c = input[i]
        if (c == '.' || c == '!' || c == '?') {
            val seee = input.substring(Ssq, i + 1).trim()
            if (seee.isNotEmpty()) {
                sen.add(seee)
            }
            Ssq = i + 1
        }
    }

    if (Ssq < input.length) {
        val last = input.substring(Ssq).trim()
        if (last.isNotEmpty()) {
            sen.add(last)
        }
    }

    val counts = IntArray(sen.size)

    for (i in sen.indices) {
        var words = 0
        var prevChar = ' '

        for (c in sen[i]) {
            if (c != ' ' && prevChar == ' ') {
                words++
            }
            prevChar = c
        }
        counts[i] = words
    }

    for (i in 1 until sen.size) {
        var j = i
        while (j > 0 && counts[j] < counts[j - 1]) {
            val ts = sen[j]
            sen[j] = sen[j - 1]
            sen[j - 1] = ts
            val tempCount = counts[j]
            counts[j] = counts[j - 1]
            counts[j - 1] = tempCount

            j--
        }
    }
    println("\nОтсортировано:")
    for (i in sen.indices) {
        println("${counts[i]} слов: ${sen[i]}")
    }
}