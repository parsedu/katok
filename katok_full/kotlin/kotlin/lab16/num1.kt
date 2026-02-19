package lab16

import kotlin.random.Random

fun randNum(size: Int, range: IntRange): IntArray {
    val numbers = range.toList()
    val shuffled = numbers.shuffled()
    return shuffled.take(size).toIntArray()
}

fun randNum(size: Int, min: Int, max: Int): IntArray? {
    if (size > max - min) {
        return null
    }

    val set = mutableSetOf<Int>()
    while (set.size < size) {
        set.add(Random.nextInt(min, max))
    }

    return set.toIntArray()
}

fun main() {
    println("Кол-во чисел -  ")
    val size = readln().toInt()

    print("Ввеедите min: ")
    val min = readln().toInt()

    print("Ввеедите max: ")
    val max = readln().toInt()

    val array = randNum(size, min, max)?.sortedArray()
    array?.forEach {
        print("$it ")
    }
//    println("Диапазон (формат 1 10) ")
//    val (min, max) = readln().split(" ").map { it.toInt() }
//
//    val res = randNum(size, min..max)
//
//    println("\nУникальные случайные числа:")
//    println(res.joinToString(", "))
}