//go:build lab8
// +build lab8

//go:build lab8
// +build lab8

package main

import (
	"fmt"
	"math"
)

func main() {

	k := 2.0
	n := 10

	fmt.Println("k =", k, ", n =", n)
	fmt.Println()

	// №1
	a1 := make([]float64, n)
	a1[0] = 1
	a1[1] = 2
	a1[2] = 0

	count1 := 0
	for i := 3; i < n; i++ {
		if a1[i-3] != 0 {
			a1[i] = (math.Exp(2*a1[i-3]) + math.Exp(4*a1[i-1])) / a1[i-3]
		} else {
			a1[i] = 0
		}
	}

	for i := 0; i < n; i++ {
		if a1[i] < 1 {
			count1++
		}
	}

	fmt.Println("1. Количество членов меньше 1:", count1)

	// №2
	a2 := make([]float64, n)
	a2[0] = 1
	a2[1] = 0
	a2[2] = 2

	count2 := 0
	for i := 3; i < n; i++ {

		a2[i] = math.Sqrt(k)*a2[i-1] + a2[i-2]*a2[i-3]
	}

	for i := 0; i < n; i++ {

		if int(math.Floor(a2[i]))%2 != 0 {
			count2++
		}
	}
	fmt.Println("2. Количество членов с нечетной целой частью:", count2)

	// №3
	a3 := make([]float64, n)
	a3[0] = 1
	a3[1] = 2
	a3[2] = 2

	sum3 := 0.0
	count3 := 0
	for i := 3; i < n; i++ {
		arg := math.Sqrt(2*k)*a3[i-3] + a3[i-1]
		a3[i] = math.Log(math.Abs(arg)) - a3[i-3]
	}

	for i := 0; i < n; i++ {
		if int(math.Floor(a3[i]))%2 != 0 {
			sum3 += a3[i]
			count3++
		}
	}

	avg3 := 0.0
	if count3 > 0 {
		avg3 = sum3 / float64(count3)
	}
	fmt.Println("3. Среднее арифметическое членов с нечетной целой частью:", avg3)

	// №4
	a4 := make([]float64, n)
	a4[0] = 1
	a4[1] = 2
	a4[2] = 3

	sum4 := 0.0
	for i := 3; i < n; i++ {
		a4[i] = math.Sin(math.Pi/k*a4[i-3]) - a4[i-1]
	}

	for i := 0; i < n; i++ {
		sum4 += a4[i]
	}

	avg4 := sum4 / float64(n)
	fmt.Println("4. Среднее арифметическое всех членов:", avg4)

	// №5
	a5 := make([]float64, n)
	a5[0] = 1
	a5[1] = 2
	a5[2] = 3

	sum5 := 0.0
	count5 := 0
	for i := 3; i < n; i++ {
		a5[i] = math.Cos(math.Pi/k*(a5[i-3]+k*k)) + a5[i-2]
	}

	for i := 0; i < n; i++ {
		if int(math.Floor(a5[i]))%2 == 0 {
			sum5 += a5[i]
			count5++
		}
	}

	avg5 := 0.0
	if count5 > 0 {
		avg5 = sum5 / float64(count5)
	}
	fmt.Println("5. Среднее арифметическое членов с четной целой частью:", avg5)

	// №6
	a6 := make([]float64, n)
	a6[0] = 1
	a6[1] = 0
	a6[2] = 3

	sum6 := 0.0
	for i := 3; i < n; i++ {
		arg := math.Pi / k * a6[i-1]
		if arg > 0 {
			a6[i] = math.Log10(arg) + a6[i-3]*a6[i-3]
		} else {
			a6[i] = a6[i-3] * a6[i-3]
		}
	}

	for i := 0; i < n; i++ {
		sum6 += a6[i]
	}

	fmt.Println("6. Сумма всех членов:", sum6)

	// №7
	a7 := make([]float64, n)
	a7[0] = 0
	a7[1] = 0
	a7[2] = 1

	prod7 := 1.0
	for i := 3; i < n; i++ {
		a7[i] = a7[i-3] - k*k + math.Abs(a7[i-2])
	}

	for i := 0; i < n; i++ {
		prod7 *= a7[i]
	}

	fmt.Println("7. Произведение всех членов:", prod7)

	// №8
	a8 := make([]float64, n)
	a8[0] = 0
	a8[1] = 1
	a8[2] = 1

	count8 := 0
	for i := 3; i < n; i++ {
		a8[i] = a8[i-3]*a8[i-3] - k*a8[i-1] + 2*math.Abs(a8[i-1])
	}

	for i := 0; i < n; i++ {
		frac := a8[i] - math.Floor(a8[i])
		if frac > 0.5 {
			count8++
		}
	}

	fmt.Println("8. Количество членов с дробной частью > 0.5:", count8)

	// №9
	a9 := make([]float64, n)
	a9[0] = 0
	a9[1] = 1
	a9[2] = 0

	count9 := 0
	for i := 3; i < n; i++ {
		a9[i] = math.Sin(a9[i-3]) - k*k + k*math.Abs(a9[i-2]) + a9[i-1]
	}

	for i := 0; i < n; i++ {
		frac := a9[i] - math.Floor(a9[i])
		if frac < 0.5 {
			count9++
		}
	}

	fmt.Println("9. Количество членов с дробной частью < 0.5:", count9)

	// №10
	a10 := make([]float64, n)
	a10[0] = 0
	a10[1] = 0
	a10[2] = 1

	count10 := 0
	for i := 3; i < n; i++ {
		a10[i] = a10[i-3] - k*k + math.Abs(a10[i-2])
	}

	for i := 0; i < n; i++ {
		if int(math.Floor(a10[i]))%2 == 0 {
			count10++
		}
	}

	fmt.Println("10.Количество членов с четной целой частью:", count10)
}
