//go:build lab9
// +build lab9

//go:build lab9
// +build lab9

package main

import (
	"fmt"
	"math"
)

func main() {
	A := []int{2, -5, 7, 0, 12, -8, 3, 9, 4, 6}
	n := len(A)

	fmt.Println("Массив:", A)
	fmt.Println()

	//№1
	sum1 := 0
	for i := 0; i < 14 && i < n; i++ {
		if A[i]%3 != 0 {
			sum1 += A[i] % 3
		}
	}
	fmt.Printf("1. Сумма остатков от деления на 3: %d\n", sum1)

	//№2
	prod2 := 1
	count2 := 0
	for i := 0; i < 13 && i < n; i++ {
		if A[i]%4 != 0 {
			prod2 *= A[i] % 4
			count2++
		}
	}
	if count2 == 0 {
		prod2 = 0
	}
	fmt.Printf("2. Произв остатков от деления на 4: %d\n", prod2)

	// №3
	sum3 := 0
	for i := 0; i < 10 && i < n; i++ {
		if A[i]%2 == 0 {
			sum3 += i
		}
	}
	fmt.Printf("3. Сумма четных элементов: %d\n", sum3)

	// №4
	prod4 := 1
	count4 := 0
	for i := 0; i < 11 && i < n; i++ {
		if A[i] > 7 {
			prod4 *= i
			count4++
		}
	}
	if count4 == 0 {
		prod4 = 0
	}
	fmt.Printf("4. Произ элементов > 7: %d\n", prod4)

	// №5
	sum5 := 0
	for i := 0; i < 14 && i < n; i++ {
		if A[i]%3 == 0 {
			sum5 += i * i
		}
	}
	fmt.Printf("5. Сумма квадратов элементов, на 3: %d\n", sum5)

	// №6
	sum6 := 0
	count6 := 0
	for i := 0; i < 12 && i < n; i++ {
		if A[i] < 0 {
			sum6 += int(math.Abs(float64(A[i])))
			count6++
		}
	}
	avg6 := 0.0
	if count6 > 0 {
		avg6 = float64(sum6) / float64(count6)
	}
	fmt.Printf("6. Ср ар модулей отрицательных: %.2f\n", avg6)

	// №7
	prod7 := 1
	count7 := 0
	for i := 0; i < 11 && i < n; i++ {
		if A[i]%2 == A[i]%3 {
			prod7 *= A[i]
			count7++
		}
	}
	if count7 == 0 {
		prod7 = 0
	}
	fmt.Printf("7. Произв с остатком от деления на 2 и на 3: %d\n", prod7)

	//№8
	sum8 := 0
	for i := 0; i < 13 && i < n; i++ {
		x := float64(A[i])
		if 4*x > x*x {
			sum8 += A[i]
		}
	}
	fmt.Printf("8. Сумма элементов 4*x > x^2: %d\n", sum8)

	//№9
	prod9 := 1.0
	count9 := 0
	for i := 0; i < 14 && i < n; i++ {
		if i%3 == 0 {
			prod9 *= float64(A[i] * A[i])
			count9++
		}
	}
	avg9 := 0.0
	if count9 > 0 {
		avg9 = math.Pow(prod9, 1.0/float64(count9))
	}
	fmt.Printf("9. Ср.геом кв кратных 3: %.2f\n", avg9)

	//№10
	sum10 := 0
	count10 := 0
	for i := 0; i < 15 && i < n; i++ {
		if i%3 == 2 {
			sum10 += A[i] * A[i]
			count10++
		}
	}
	avg10 := 0.0
	if count10 > 0 {
		avg10 = float64(sum10) / float64(count10)
	}
	fmt.Printf("10. Ср. ар. кв элементов с остатком 2 делении на 3: %.2f\n", avg10)
}
