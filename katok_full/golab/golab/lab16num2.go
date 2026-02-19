package main

import "fmt"

func soverNum(n int) bool {
	switch n {
	case 6, 28, 496, 8128, 33550336:
		return true
	default:
		return false
	}
}

func main() {
	var start, end int

	fmt.Print("Начало диапазона: ")
	fmt.Scan(&start)

	fmt.Print("Конец диапазона: ")
	fmt.Scan(&end)

	fmt.Printf("\nПроверка чисел от %d до %d:\n", start, end)

	count := 0
	for num := start; num <= end; num++ {
		if soverNum(num) {
			fmt.Printf("%d - Господи, ничего совершеннее этого числа не видел\n", num)
			count++
		} else {
			fmt.Printf("%d - ужас, какое не совершенное число\n", num)
		}
	}
}
