package lab9
fun main() {

    print("Введите сторону a: ")
    val a = readln().toDouble()
    print("Введите сторону b: ")
    val b = readln().toDouble()
    print("Введите сторону c: ")
    val c = readln().toDouble()

    if (a + b > c && a + c > b && b + c > a) {
        println("Треугольник существует.")
        when {
            a == b && b == c -> println("Треугольник равносторонний.")
            a == b || a == c || b == c -> println("Треугольник равнобедренный.")
            else -> println("Треугольник разносторонний.")
        }
    } else {
            println("Треугольник не существует.")
        }

}