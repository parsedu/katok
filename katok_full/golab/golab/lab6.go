//go:build lab6
// +build lab6

//go:build lab6
// +build lab6

package main

import (
	"fmt"
	"math"
)

func main() {
	var x float64 = 3.0
	var k float64 = 2.0

	var result float64

	// №1
	result = 1.0
	for n := 1; n <= 5; n++ {
		value := 2*x - float64(n*n)
		result *= value

	}
	fmt.Printf("1. P = %.4f\n", result)

	// №2
	result = 0.0
	for n := 1; n <= 4; n++ {
		value := math.Sin(math.Pi * float64(n) / 9)
		result += value

	}
	fmt.Printf("2. S = %.4f\n", result)

	// №3
	result = 1.0
	for n := 1; n <= 5; n++ {
		value := 1 + math.Sin(float64(n)*math.Pi/k)
		result *= value
	}
	fmt.Printf("3. P = %.4f\n", result)

	// №4
	result = 0.0
	for n := 1; n <= 4; n++ {
		value := math.Sqrt(float64(n)) * math.Cos(math.Pi*float64(n)/8)
		result += value
	}
	fmt.Printf("4. S = %.4f\n", result)

	// №5
	result = 1.0
	for n := 1; n <= 4; n++ {
		num := 1 + float64(n)
		den := 1 + math.Sqrt(x*x+float64(n*n))
		value := num / den
		result *= value
	}
	fmt.Printf("5. P = %.4f\n", result)

	// №6
	result = 0.0
	for n := 1; n <= 4; n++ {
		num := 2 + float64(n*n*n)
		den := math.Sqrt(x*x + float64(n*n))
		value := num / den
		result += value
	}
	fmt.Printf("6. S = %.4f\n", result)

	// №7
	result = 1.0
	for n := 1; n <= 5; n++ {
		num := 2 + float64(n)
		den := 2 + math.Sqrt(float64(n*n*n))
		value := num / den
		result *= value
	}
	fmt.Printf("7. P = %.4f\n", result)

	// №8
	result = 0.0
	for n := 1; n <= 4; n++ {
		num := 1 + math.Sqrt(float64(n*n*n))
		den := math.Sqrt(1 + float64(n*n))
		value := num / den
		result += value
	}
	fmt.Printf("8. S = %.4f\n", result)

	// №9
	result = 1.0
	for n := 1; n <= 4; n++ {
		num := float64(n)
		den := 1 + math.Sqrt(float64(n*n*n))
		value := num / den
		result *= value
	}
	fmt.Printf("9. P = %.4f\n", result)

	// №10
	result = 0.0
	for n := 1; n <= 4; n++ {
		num := math.Exp(float64(n))
		den := float64(n * n * n)
		value := num / den
		result += value
	}
	fmt.Printf("10. S = %.4f\n", result)
}
