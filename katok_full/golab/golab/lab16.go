package main

import (
	"fmt"
	"math/rand"
	"time"
)

func RanNum(size int, min, max int) []int {
	rand.New(rand.NewSource(time.Now().UnixNano()))

	num := make([]int, 0, max-min+1)
	for i := min; i <= max; i++ {
		num = append(num, i)
	}

	rand.Shuffle(len(num), func(i, j int) {
		num[i], num[j] = num[j], num[i]
	})

	if size > len(num) {
		return num
	}
	return num[:size]
}

func main() {
	var size, min, max int

	fmt.Print("Кол-во чисел: ")
	fmt.Scan(&size)

	fmt.Print("Диапазон: ")
	fmt.Scan(&min, &max)

	res := RanNum(size, min, max)

	fmt.Println("\nМассив:")
	for i, num := range res {
		if i > 0 {
			fmt.Print(", ")
		}
		fmt.Print(num)
	}
	fmt.Println()
}
