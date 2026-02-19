package lab9

fun main(){
    //№1
    val text = " Один пробел "
    val bz = text.trim()
    println("№1 $bz")

    //№2
    val ccp = 25
    val sp = " ".repeat(ccp)
    val res = "Тута>${sp}<Тама"
    println("№2 $res")

    //11
    val text2 = "тутутутутутут"
    val tex = text2.padStart(120)
    println(tex)
}