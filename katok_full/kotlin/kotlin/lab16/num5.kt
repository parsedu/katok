package lab16

fun sumDel(number: Int): Int {
    if (number <= 0) return 0
    var sum = 0
    for (i in 1..number) {
        if (number % i == 0) {
            sum += i
            println(i)
        }
    }
    return sum
}

fun main() {
    println("Введите число:")
    val number = readln().toInt()
    val sum = sumDel(number)
    println("Сумма всех делителей числа $number = $sum")
}