package lab9

import java.util.*

fun main(){
    val text = "очень маленькие буквы, превращаются в большие букавки"
    val bigBukva = text.uppercase(Locale.getDefault())
    println(bigBukva)
}