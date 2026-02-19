package lab19

fun main() {
    //Программа раз
    val result = "А".repeat(10)
    println(result)
    //Программа два)
    println("AAAAAAAAAA")
    //можно как и в программе раз, но будет это программа три
    println("А".repeat(10))

    //Вот такие способы еще есть в интернетах через диапазон и массив
    val aaaa = (1..10).joinToString("") { "А" }
    println("$aaaa")

    val aaaaaaa = Array(10) { "А" }.joinToString("")
    println("$aaaaaaa")
}