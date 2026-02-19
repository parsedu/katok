//go:build lab12
// +build lab12

package main

import (
	"fmt"
	"math"
)

func main() {
	const n, m = 5, 5
	var A [n][m]int
	var rows, cols int
	var sum, count int
	var prod, geom float64
	var hN bool

	fmt.Println("№1:")
	rows, cols = 5, 2

	A = [5][5]int{
		{1, -2},
		{-3, 4},
		{5, -6},
		{-7, 8},
		{9, -10},
	}
	sum = 0
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if A[i][j] < 0 {
				sum += -A[i][j]
			}
		}
	}
	fmt.Println("Сумма модулей отрицательных элементов:", sum)

	fmt.Println("№2:")
	rows, cols = 2, 5

	A = [5][5]int{
		{-1, 2, -3, 4, -5},
		{6, -7, 8, -9, 10},
	}
	geom = 1.0
	count = 0
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if A[i][j] < 0 {
				geom *= float64(-A[i][j])
				count++
			}
		}
	}
	if count > 0 {
		geom = math.Pow(geom, 1.0/float64(count))
		fmt.Printf("Среднее геометрическое модулей отрицательных: %.4f\n", geom)
	} else {
		fmt.Println("Отрицательных элементов нет")
	}

	fmt.Println("№3:")
	rows, cols = 3, 4

	A = [5][5]int{
		{1, 2, 3, 4},
		{5, 6, 7, 8},
		{9, 10, 11, 12},
	}
	geom = 1.0
	count = 0
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if A[i][j]%2 != 0 {
				geom *= float64(A[i][j] * A[i][j])
				count++
			}
		}
	}
	if count > 0 {
		geom = math.Pow(geom, 1.0/float64(count))
		fmt.Printf("Среднее геометрическое квадратов нечётных: %.4f\n", geom)
	} else {
		fmt.Println("Нечётных элементов нет")
	}

	fmt.Println("№4:")
	rows, cols = 3, 4
	A = [5][5]int{
		{2, 5, 8, 11},
		{14, -1, -4, 17},
		{20, 23, 26, 29},
	}
	count = 0
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if A[i][j]%3 == 2 || (A[i][j] < 0 && A[i][j]%3 == -1) {
				count++
			}
		}
	}
	fmt.Println("Количество элементов с остатком 2 при делении на 3:", count)

	fmt.Println("№5:")
	rows, cols = 4, 3

	A = [5][5]int{
		{1, 2, 3},
		{4, 5, 6},
		{7, 8, 9},
		{10, 11, 12},
	}
	sum = 0
	count = 0
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			mod := A[i][j] % 4
			if mod < 0 {
				mod += 4
			}
			if mod == 1 || mod == 3 {
				sum += A[i][j]
				count++
			}
		}
	}
	if count > 0 {
		fmt.Printf("Среднее арифметическое: %.4f\n", float64(sum)/float64(count))
	} else {
		fmt.Println("Нет элементов с остатком 1 или 3 при делении на 4")
	}

	fmt.Println("№6:")
	rows, cols = 3, 5
	A = [5][5]int{
		{1, -2, 3, -4, 5},
		{6, -7, 8, -9, 10},
		{0, 3, -2, 7, -1},
	}
	prod = 1.0
	hN = false
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			absVal := int(math.Abs(float64(A[i][j])))
			if absVal >= 1 && absVal <= 5 {
				prod *= float64(A[i][j])
				hN = true
			}
		}
	}
	if hN {
		fmt.Printf("Произведение элементов с модулем в [1,5]: %.4f\n", prod)
	} else {
		fmt.Println("Нет элементов с модулем в диапазоне [1,5]")
	}

	fmt.Println("№7:")
	rows, cols = 4, 3
	A = [5][5]int{
		{0, 6, -6},
		{7, -7, 8},
		{-8, 9, -9},
		{10, -10, 0},
	}
	prod = 1.0
	count = 0
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			absVal := int(math.Abs(float64(A[i][j])))
			if absVal < 1 || absVal > 5 {
				prod *= float64(A[i][j])
				count++
			}
		}
	}
	if count > 0 {
		fmt.Printf("Произведение элементов с модулем вне [1,5]: %.4f\n", prod)
	} else {
		fmt.Println("Все элементы в диапазоне [1,5]")
	}

	fmt.Println("№8:")
	rows, cols = 5, 3

	A = [5][5]int{
		{0, 1, 2},
		{3, 4, 5},
		{6, 7, 8},
		{9, 10, 11},
		{12, 13, 14},
	}
	count = 0
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {

			if (i > 0 && A[i][j]%i == 0) || (j > 0 && A[i][j]%j == 0) {
				count++
			}
		}
	}
	fmt.Println("Количество элементов, делящихся на свой индекс:", count)

	fmt.Println("№9:")
	rows, cols = 3, 5
	A = [5][5]int{
		{2, 3, 4, 5, 6},
		{7, 8, 9, 10, 11},
		{12, 13, 14, 15, 16},
	}
	count = 0
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if (i+j)%2 == 0 && A[i][j]%2 == 0 {
				count++
			}
		}
	}
	fmt.Println("Количество чётных элементов на чётных суммах индексов:", count)

	fmt.Println("№10:")
	rows, cols = 3, 4

	A = [5][5]int{
		{1, 2, 4, 5},
		{7, 8, 10, 11},
		{13, 14, 16, 17},
	}
	sum = 0
	for i := 0; i < rows; i++ {
		for j := 0; j < cols; j++ {
			if A[i][j]%3 != 0 {
				mod := A[i][j] % 3
				if mod < 0 {
					mod += 3
				}
				sum += mod
			}
		}
	}
	fmt.Println("Сумма остатков от деления на 3 некратных трём элементов:", sum)
}
