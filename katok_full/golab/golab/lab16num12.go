package main

import "fmt"

func kakoitoFinabichi(n int) int64 {
	if n <= 0 {
		return 0
	}
	if n == 1 {
		return 1
	}

	fib := make([]int64, n)
	fib[0] = 1
	fib[1] = 1

	for i := 2; i < n; i++ {
		fib[i] = fib[i-1] + fib[i-2]
	}

	var sum int64 = 0
	for i := 0; i < n; i++ {
		sum += fib[i]
	}

	return sum
}

func main() {
	var n int

	fmt.Println("Введите N:")
	fmt.Scan(&n)

	sum := kakoitoFinabichi(n)
	fmt.Printf("Сумма первых %d чисел Фибоначчи: %d\n", n, sum)
}
