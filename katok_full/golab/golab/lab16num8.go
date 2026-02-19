package main

import (
	"fmt"
	"math"
)

func prostoeCh(n int) bool {
	if n <= 1 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}

	limit := int(math.Sqrt(float64(n)))
	for i := 3; i <= limit; i += 2 {
		if n%i == 0 {
			return false
		}
	}

	return true
}

func main() {
	var start, end int

	fmt.Print("Начало: ")
	fmt.Scan(&start)

	fmt.Print("Конец: ")
	fmt.Scan(&end)

	count := 0
	for num := start; num <= end; num++ {
		isPrime := prostoeCh(num)
		if isPrime {
			fmt.Printf("%d - Простое\n", num)
			count++
		} else {
			fmt.Printf("%d - Составное\n", num)
		}
	}

	fmt.Printf("\nНайдено простых чисел: %d\n", count)
}
