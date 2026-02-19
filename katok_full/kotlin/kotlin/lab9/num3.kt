package lab9
fun main() {
    val text = "ааааааааааааааааааааааааааааааааааааааааааааа"
    val dl = 150

    fun ceS(input: String, dl: Int): String {
        if (input.length >= dl) return input
        val pravo = (dl - input.length) / 2
        val levo = dl - input.length - pravo
        return " ".repeat(pravo) + input + " ".repeat(levo)
    }
    val centered = ceS(text, dl)
    println(centered)
}