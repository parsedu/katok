package lab9

fun main() {
    val text = "Првиет    меня    зовут   Максим  !"
    val res = text.replace("\\s+".toRegex(), " ")
    println(res)
}