package lab9
fun main(){
    val text = "ща буду бить слова ... на ентры"
    val words = text.split(" ")
        for (word in words) {
            println(word)
    }
}