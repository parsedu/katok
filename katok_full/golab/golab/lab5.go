//go:build lab5
// +build lab5

//go:build lab5
// +build lab5

package main

import (
	"fmt"
	"math"
)

func main() {

	var a, b, c, d, x, y int
	var k, m, n float64

	fmt.Println("№1")

	a = 23
	b = 34

	fmt.Printf("исход: %d и %d\n", a, b)
	a1 := a / 10
	a2 := a % 10

	b1 := b / 10
	b2 := b % 10

	count := 0
	fmt.Print("Одинаковые: ")

	if a1 == b1 || a1 == b2 {
		fmt.Printf("%d ", a1)
		count++
	}
	if a2 == b1 || a2 == b2 {
		if a2 != a1 || (a2 == b1 && a2 != b2) || (a2 == b2 && a2 != b1) {
			fmt.Printf("%d ", a2)
			count++
		}
	}

	if count == 0 {
		fmt.Print("нет")
	}
	fmt.Printf("\nВсего цифр: %d\n", count)
	fmt.Println()

	fmt.Println("№2")
	a = 537

	fmt.Printf("Число: %d\n", a)

	c = a / 100
	d = (a / 10) % 10
	x = a % 10

	if c > x {
		fmt.Println("Первая цифра больше")
		if d%2 == 0 {
			fmt.Printf("Средняя цифра %d четная\n", d)
			y = d / 2
			fmt.Printf("0.5средней цифры: %d\n", y)
		} else {
			fmt.Printf("Средняя цифра %d нечетная\n", d)
		}
	} else if x > c {
		fmt.Println("Последняя цифра наибольшая")
	} else {
		fmt.Println("Первая и последняя цифры равны")
	}
	fmt.Println()

	fmt.Println("№3")
	a = 426

	fmt.Printf("Число: %d\n", a)

	c = a / 100
	d = (a / 10) % 10
	x = a % 10

	if c < d {
		fmt.Println("Первая цифра наименьшая")
		b = d*100 + c*10 + x
		fmt.Printf("После замены: %d\n", b)
	} else if d < c {
		fmt.Println("Вторая цифра наименьшая")
		b = a
	} else {
		fmt.Println("Первая и вторая цифры равны")
		b = a
	}

	if b%3 == 0 {
		fmt.Printf("Число %d кратно 3\n", b)
	} else {
		fmt.Printf("Число %d не кратно 3\n", b)
	}
	fmt.Println()

	fmt.Println("№4")
	a = 369

	fmt.Printf("Число: %d\n", a)

	c = a / 100
	d = (a / 10) % 10
	x = a % 10
	y = c + d + x

	if y%9 == 0 {
		fmt.Printf("Сумма цифр %d делится на 9\n", y)
		b = a / 3
		fmt.Printf("Число после деления на 3: %d\n", b)

		if b%2 == 0 {
			c = b / 2
			fmt.Printf("Четное, делим пополам: %d\n", c)
		} else {
			c = b * 2
			fmt.Printf("Нечетное, удваиваем: %d\n", c)
		}
	} else {
		fmt.Printf("Сумма цифр %d не делится на 9\n", y)
	}
	fmt.Println()

	fmt.Println("№5")
	a = 123321

	fmt.Printf("Число: %d\n", a)

	c = a / 1000
	x = c/100 + (c/10)%10 + c%10

	d = a % 1000
	y = d/100 + (d/10)%10 + d%10

	if x == y {
		fmt.Println("счастливое")
		if x == 11 || x == 22 {
			fmt.Println("супер-пуперм-мега-очень-счастливое")
		} else {
			fmt.Printf("Сумма цифр: %d (не 11 и не 22)\n", x)
		}
	} else {
		fmt.Println("обычное")
		fmt.Printf("Суммы: %d и %d\n", x, y)
	}
	fmt.Println()

	fmt.Println("№6")
	a = 4728

	fmt.Printf("Число: %d\n", a)

	has2 := false
	has7 := false
	pos2 := 0
	pos7 := 0

	temp := a
	pos := 4

	for temp > 0 {
		digit := temp % 10
		if digit == 2 {
			has2 = true
			pos2 = pos
		}
		if digit == 7 {
			has7 = true
			pos7 = pos
		}
		temp = temp / 10
		pos--
	}

	if !has2 && !has7 {
		fmt.Println("Нет ни двоек, ни семёрок, ни выходных, ни отдыха, еще и спать хочется...")
	} else if has2 && has7 {
		if pos2 > pos7 {
			fmt.Println("2 стоит перед 7")
		} else if pos7 > pos2 {
			fmt.Println("7 стоит перед 2")
		} else {
			fmt.Println("2 и 7 на одной позиции")
		}
	} else if has2 {
		fmt.Println("Есть только 2")
	} else if has7 {
		fmt.Println("Есть только 7")
	}
	fmt.Println()

	fmt.Println("№7")
	m = 5.0
	n = 3.0

	fmt.Printf("m=%.1f, n=%.1f\n", m, n)

	if m*m >= n*n {
		k = math.Sqrt(m*m - n*n)
		fmt.Printf("k = %.3f\n", m, n, k)

		if k <= 1 {
			z := math.Asin(k)
			fmt.Printf("Z = %.3f\n", k, z)
		} else {
			z := math.Asin(1 / k)
			fmt.Printf("Z = %.3f\n", k, z)
		}
	} else {
		z := math.Log(n*n - m*m)
		fmt.Printf("Z = %.3f\n", n, m, z)
	}
	fmt.Println()

	fmt.Println("№8")
	a = 10
	b = 7
	c = 15
	d = 12

	fmt.Printf("Цыфарки: %d, %d, %d, %d\n", a, b, c, d)

	max := a
	if b > max {
		max = b
	}
	if c > max {
		max = c
	}
	if d > max {
		max = d
	}

	fmt.Printf("Наибольшее: %d\n", max)

	result := float64(max) / 5.0
	fmt.Printf("уменшение в 5 раз: %.1f\n", result)
	fmt.Println()

	fmt.Println("№9")
	a = -7

	fmt.Printf("Число: %d\n", a)

	if a == 0 {
		fmt.Println("0")
	} else if a > 0 {
		if a%2 == 0 {
			fmt.Println("положительное четное")
		} else {
			fmt.Println("положительное нечетное")
		}
	} else {
		if a%2 == 0 {
			fmt.Println("отрицательное четное")
		} else {
			fmt.Println("отрицательное нечетное")
		}
	}
	fmt.Println()

	fmt.Println("№10")
	a = 123

	fmt.Printf("Число: %d\n", a)

	digits := 0
	if a >= 100 {
		digits = 3
	} else if a >= 10 {
		digits = 2
	} else {
		digits = 1
	}

	desc := ""
	if a%2 == 0 {
		desc = "четное "
	} else {
		desc = "нечетное "
	}

	if digits == 1 {
		desc += "однозначное "
	} else if digits == 2 {
		desc += "двузначное "
	} else {
		desc += "трехзначное "
	}

	desc += "число"
	fmt.Println(desc)
}
