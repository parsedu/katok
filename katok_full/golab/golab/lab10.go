//go:build lab10
// +build lab10

package main

import "fmt"

func main() {
	arr := []int{12, -5, 8, 17, -3, 9, 22, -14, 6, 10, -7, 4, 15}
	n := len(arr)

	fmt.Println("№1:")
	fmt.Println("До:", arr)
	for i := 2; i < n; i += 3 {
		arr[i] *= i
	}
	fmt.Println("После:", arr)
	arr = []int{12, -5, 8, 17, -3, 9, 22, -14, 6, 10, -7, 4, 15}

	fmt.Println("\n№2:")
	fmt.Println("   До:", arr)
	for i := 1; i < n; i += 2 {
		arr[i] /= 2
	}
	fmt.Println("После:", arr)

	arr = []int{12, -5, 8, 17, -3, 9, 22, -14, 6, 10, -7, 4, 15}

	fmt.Println("\n№3:")
	fmt.Println("До:", arr)
	for i := 0; i < n; i++ {
		if arr[i]%3 == 2 {
			arr[i]++
		}
	}
	fmt.Println("После:", arr)

	arr = []int{12, -5, 8, 17, -3, 9, 22, -14, 6, 10, -7, 4, 15}

	fmt.Println("\n№4:")
	fmt.Println("До:", arr)
	for i := 0; i < n; i++ {
		if arr[i] > 10 || arr[i] < -10 {
			arr[i] = 0
		}
	}
	fmt.Println("После:", arr)

	arr = []int{12, -5, 8, 17, -3, 9, 22, -14, 6, 10, -7, 4, 15}

	fmt.Println("\n№5:")
	fmt.Println("До:", arr)
	for i := 1; i < n; i += 2 {
		if arr[i] < 0 {
			arr[i] *= arr[i]
		}
	}
	fmt.Println("После:", arr)

	arr = []int{12, -5, 8, 17, -3, 9, 22, -14, 6, 10, -7, 4, 15}

	fmt.Println("\n№6:")
	fmt.Println("До:", arr)
	for i := 1; i < n; i += 2 {
		arr[i] = arr[i] % 10
	}
	fmt.Println("После:", arr)

	arr = []int{12, -5, 8, 17, -3, 9, 22, -14, 6, 10, -7, 4, 15}

	fmt.Println("\n№7:")
	fmt.Println("До:", arr)
	for i := 0; i < n; i++ {
		if i%2 == 0 {
			arr[i] = arr[i] % 7
		}
	}
	fmt.Println("После:", arr)

	arr = []int{12, -5, 8, 17, -3, 9, 22, -14, 6, 10, -7, 4, 15}

	fmt.Println("\n№8:")
	fmt.Println("До:", arr)
	for i := 2; i < n; i += 3 {
		arr[i] = arr[i] % 2
	}
	fmt.Println("После:", arr)

	arr = []int{12, -5, 8, 17, -3, 9, 22, -14, 6, 10, -7, 4, 15}

	fmt.Println("\n№9:")
	fmt.Println("До:", arr)
	for i := 1; i < n; i += 2 {
		arr[i] = arr[i] / 5
	}
	fmt.Println("После:", arr)

	arr = []int{12, -5, 8, 17, -3, 9, 22, -14, 6, 10, -7, 4, 15}

	fmt.Println("\n№10:")
	fmt.Println("До:", arr)
	for i := 0; i < n; i++ {
		if arr[i] < 0 {
			arr[i] = arr[i] / 3
		}
	}
	fmt.Println("После:", arr)
}
