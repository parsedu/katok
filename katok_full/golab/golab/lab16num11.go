package main

import (
	"fmt"
	"math/rand"
	"time"
)

func randomBukva(size int) []byte {
	res := make([]byte, size)

	for i := 0; i < size; i++ {
		ranBukva := 'A' + byte(rand.Intn(26))
		res[i] = ranBukva
	}

	return res
}

func main() {
	rand.Seed(time.Now().UnixNano())

	var size int

	fmt.Println("Введите размер массива:")
	fmt.Scan(&size)

	letters := randomBukva(size)

	fmt.Println("\nМассив:")
	fmt.Print("[")
	for i, letter := range letters {
		if i > 0 {
			fmt.Print(" ")
		}
		fmt.Printf("%c", letter)
	}
	fmt.Println("]")
}
