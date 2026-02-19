package lab16

fun zZodiak(day: Int, month: Int): String {
    return when (month) {
        1 -> if (day <= 20) "Козерог" else "Водолей"
        2 -> if (day <= 19) "Водолей" else "Рыбы"
        3 -> if (day <= 20) "Рыбы" else "Овен"
        4 -> if (day <= 20) "Овен" else "Телец"
        5 -> if (day <= 21) "Телец" else "Близнецы"
        6 -> if (day <= 21) "Близнецы" else "Рак"
        7 -> if (day <= 22) "Рак" else "Лев"
        8 -> if (day <= 23) "Лев" else "Дева"
        9 -> if (day <= 23) "Дева" else "Весы"
        10 -> if (day <= 23) "Весы" else "Скорпион"
        11 -> if (day <= 22) "Скорпион" else "Стрелец"
        12 -> if (day <= 21) "Стрелец" else "Козерог"
        else -> "Неверный месяц"
    }
}

fun main() {
    println("Введите день рождения:")
    val day = readln().toInt()

    println("Введите месяц рождения:")
    val month = readln().toInt()

    val sign = zZodiak(day, month)
    println("Поздравляю вы: $sign")
}