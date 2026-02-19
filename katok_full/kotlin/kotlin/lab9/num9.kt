package lab9

fun main(){
    val date = "10.12.2025"
    val (day, month, year) = date.split(".")
    println(day)
    println(month)
    println(year)
}