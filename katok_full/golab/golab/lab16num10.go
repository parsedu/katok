package main

import "fmt"

func soArr(a, b int) []int {
	start := a
	end := b

	if a > b {
		start = b
		end = a
	}

	size := end - start + 1
	result := make([]int, size)

	for i := 0; i < size; i++ {
		result[i] = start + i
	}

	return result
}

func main() {
	var num1, num2 int

	fmt.Println("Введите два числа (через пробел):")
	fmt.Scan(&num1, &num2)

	result := soArr(num1, num2)

	fmt.Println("\nРезультат:")

	min := num1
	max := num2
	if num1 > num2 {
		min = num2
		max = num1
	}

	fmt.Printf("От: %d\n", min)
	fmt.Printf("До: %d\n", max)

	fmt.Print("Массив: [")
	for i, val := range result {
		if i > 0 {
			fmt.Print(", ")
		}
		fmt.Print(val)
	}
	fmt.Println("]")
}
