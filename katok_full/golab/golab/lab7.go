//go:build lab7
// +build lab7

package main

import (
	"fmt"
	"math"
)

func main() {
	var x, result, start, end, step, temp1, temp2 float64

	fmt.Println("№1")
	start = -3.5
	end = 6.0
	step = 0.7

	x = start
	for x <= end+0.001 {
		temp1 = math.Pow(8, x)
		temp2 = math.Sin(x)
		temp1 = temp1 * temp2

		if temp1 >= 0 {
			result = math.Sqrt(temp1)
			whole := math.Floor(result)
			frac := result - whole
			if frac < 0 {
				frac = -frac
			}

			check := "Не привышает"
			if frac > 0.5 {
				check = "Привышает"
			}

			fmt.Printf("%.1f\t%.4f\t%s\n", x, result, check)
		} else {
			fmt.Printf("%.1f\tНет корня\n", x)
		}

		x = x + step
	}
	fmt.Println()

	fmt.Println("№2")
	start = -5.0
	end = 8.0
	step = 1.2
	x = start
	for x <= end+0.001 {
		temp1 = math.Sin(x)
		temp2 = 1 - temp1
		temp1 = x - temp2
		temp2 = math.Exp(temp1)

		if temp2 >= 0 {
			result = math.Sqrt(temp2)

			whole := math.Floor(result)
			frac := result - whole
			if frac < 0 {
				frac = -frac
			}

			check := "Не привышает"
			if frac > 0.5 {
				check = "Привышает"
			}

			fmt.Printf("%.1f\t%.4f\t%s\n", x, result, check)
		} else {
			fmt.Printf("%.1f\tНет корня\n", x)
		}

		x = x + step
	}
	fmt.Println()

	fmt.Println("№3")
	start = -2.5
	end = 7.0
	step = 0.6

	x = start
	for x <= end+0.001 {
		temp1 = math.Pow(3, x)
		temp2 = math.Pow(2, x)
		result = temp1 + temp2

		if result >= 0 {
			result = math.Sqrt(result)

			whole := math.Floor(result)
			intWhole := int(whole)

			rem3 := intWhole % 3
			rem4 := intWhole % 4

			check := "Не привышает"
			if rem3 > rem4 {
				check = "Привышает"
			}

			fmt.Printf("%.1f\t%.4f\t%s\n",
				x, result, check)
		} else {
			fmt.Printf("%.1f\tНет корня\n", x)
		}

		x = x + step
	}
	fmt.Println()

	fmt.Println("№4")
	start = -3.5
	end = 6.0
	step = 0.7
	k := 2.0

	x = start
	for x <= end+0.001 {
		temp1 = math.Pow(8, x)
		temp2 = x * x
		cosVal := math.Cos(temp2)
		sinVal := math.Sin(x)
		temp2 = cosVal + sinVal
		result = temp1 * temp2

		if result >= 0 {
			result = math.Sqrt(result)

			compare := k * math.Sin(x)
			if compare < 0 {
				compare = -compare
			}

			check := "Не привышает"
			if result > compare {
				check = "Привышает"
			}

			fmt.Printf("%.1f\t%.4f\t%.2f*sin=%.4f, %s\n",
				x, result, k, compare, check)
		} else {
			fmt.Printf("%.1f\tНет корня\n", x)
		}

		x = x + step
	}
	fmt.Println()

	fmt.Println("№5")
	start = -1.5
	end = 6.0
	step = 0.4

	x = start
	for x <= end+0.001 {
		temp1 = x * x
		temp2 = math.Pow(3, -temp1)
		cosVal := math.Pow(2, -temp1)
		result = temp2 + cosVal

		if result >= 0 {
			result = math.Sqrt(result)

			compare := 0.5 * math.Cos(x)
			if compare < 0 {
				compare = -compare
			}

			check := "Не привышает"
			if result > compare {
				check = "Привышает"
			}

			fmt.Printf("%.1f\t%.4f\t0.5*cos=%.4f, %s\n",
				x, result, compare, check)
		} else {
			fmt.Printf("%.1f\tНет корня\n", x)
		}

		x = x + step
	}
	fmt.Println()

	fmt.Println("№6")
	start = -1.5
	end = 5.0
	step = 0.4

	x = start
	for x <= end+0.001 {
		temp1 = math.Pow(2, x)
		temp2 = x * x
		sinVal := temp2 + x - 1
		result = temp1 * sinVal

		whole := math.Floor(result)
		intWhole := int(whole)

		rem2 := intWhole % 2
		rem3 := intWhole % 3

		check := "Не привышает"
		if rem2 > rem3 {
			check = "Привышает"
		}

		fmt.Printf("%.1f\t%.4f\t%s\n",
			x, result, check)

		x = x + step
	}
	fmt.Println()

	fmt.Println("№7")
	start = -3.0
	end = 3.0
	step = 0.35

	x = start
	for x <= end+0.001 {
		if x == 0 {
			fmt.Printf("%.2f\tДеление на 0!\n", x)
			x = x + step
			continue
		}

		temp1 = 1.0 / (x * x)
		temp2 = math.Cos(x)
		if temp2 < 0 {
			temp2 = -temp2
		}

		formula := "1"
		if temp2 > temp1 {
			result = temp1 + (x * x)
			result = math.Sqrt(result)
			formula = "1"
		} else {
			result = temp1 - temp2
			if result >= 0 {
				result = math.Sqrt(result)
				formula = "2"
			} else {
				result = math.NaN()
				formula = "2 (нет корня)"
			}
		}

		if math.IsNaN(result) {
			fmt.Printf("%.2f\tНет корня\tФ %s\n", x, formula)
		} else {
			fmt.Printf("%.2f\t%.4f\t\tФ %s\n", x, result, formula)
		}

		x = x + step
	}
	fmt.Println()

	fmt.Println("№8")
	start = -3.0
	end = 3.0
	step = 0.5
	aValue := 2.0

	x = start
	for x <= end+0.001 {
		temp1 = x * x
		temp2 = 2*temp1 - 4*x - 4

		if math.Abs(temp2) < 0.000001 {
			result = aValue * 1.0
			fmt.Printf("%.1f\t%.4f\t(использован предел sin(0)/0=1)\n", x, result)
		} else {
			sinVal := math.Sin(temp2)
			result = aValue * sinVal / temp2
			fmt.Printf("%.1f\t%.4f\n", x, result)
		}

		x = x + step
	}
	fmt.Println()

	fmt.Println("№9")
	var kInt int
	aInt := 5

	for kInt = -10; kInt <= 10; kInt++ {
		if kInt == 0 {
			fmt.Printf("%d\tДеление на 0\n", kInt)
			continue
		}

		if kInt%2 == 0 {
			result := float64(aInt) + float64(12/kInt)
			fmt.Printf("%d\t%.1f\t\tЧетное\n", kInt, result)
		} else {
			result := float64(kInt * kInt)
			fmt.Printf("%d\t%.1f\t\tНе четное\n", kInt, result)
		}
	}
	fmt.Println()

	fmt.Println("№10")
	for kInt = -4; kInt <= 8; kInt++ {
		if kInt%2 == 0 {
			result := float64(kInt+aInt) * float64(kInt+aInt)
			fmt.Printf("%d\t%.1f\t\tЧетное\n", kInt, result)
		} else {
			result := kInt % 3
			fmt.Printf("%d\t%d\t\tНе четное\n", kInt, result)
		}
	}
}
