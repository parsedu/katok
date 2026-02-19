//go:build lab4
// +build lab4

package main

import (
	"fmt"
	"math"
)

func main() {

	var a, b, r, h, x, y, z float64

	fmt.Println("№1")

	a = 10.0
	r = 4.0

	if 2*r <= a {
		x = a * a
		y = math.Pi * r * r
		z = x - y
		fmt.Printf("Площадь квадрата: %.2f, круга: %.2f\n", x, y)
		fmt.Printf("Обрезки: %.2f\n", z)
	} else {
		fmt.Printf("Вырезать нельзя. Квадрат a=%.1f, круг r=%.1f\n", a, r)
	}
	fmt.Println()

	fmt.Println("№2")
	a = 8.0
	r = 3.0

	if 2*r <= a {
		x = a * a * a
		y = (4.0 / 3.0) * math.Pi * r * r * r
		z = x - y
		fmt.Printf("Куб a=%.1f, шар r=%.1f\n", a, r)
		fmt.Printf("Объем куба: %.2f, шара: %.2f\n", x, y)
		fmt.Printf("Обрезки: %.2f\n", z)
	} else {
		fmt.Printf("Вырезать нельзя. Куб a=%.1f, шар r=%.1f\n", a, r)
	}
	fmt.Println()

	fmt.Println("№3")
	a = 5.0
	b = 4.0
	x = 6.0
	y = 3.0

	z = a * b
	h = x * y

	if z == h {
		fmt.Printf("S = : %.1f\n", z)
	} else {
		r = math.Abs(z - h)
		fmt.Printf("Прямоугольник 1: %.1fx%.1f=%.1f\n", a, b, z)
		fmt.Printf("Прямоугольник 2: %.1fx%.1f=%.1f\n", x, y, h)
		fmt.Printf("Разность: %.1f\n", r)
	}
	fmt.Println()

	fmt.Println("№4")
	h = 10.0
	r = 3.0
	x = 300.0

	y = math.Pi * r * r * h

	if x <= y {
		fmt.Printf("Вода x=%.1f помещается в стакан h=%.1f, r=%.1f\n", x, h, r)
		fmt.Printf("Объем стакана: %.1f\n", y)
	} else {
		z = x - y
		fmt.Printf("Вода x=%.1f перельется же\n", x)
		fmt.Printf("Объем стакана: %.1f, перельется: %.1f\n", y, z)
	}
	fmt.Println()

	fmt.Println("№5")
	x = 5.0
	y = 10.0

	z = x*0.25 + y*0.10

	if z >= 2.0 {
		fmt.Printf("Проговорил на %.2f у.е. \n", z)
	} else {
		a = 2.5 - z
		b = a / 0.25
		fmt.Printf("Проговорил только %.2f у.е.\n", z)
		fmt.Printf("До 2.5 не хватает %.2f у.е.\n", a)
		fmt.Printf("Минут по 0.25 не хватает: %.1f\n", b)
	}
	fmt.Println()

	fmt.Println("№6")
	x = 15.0

	if x <= 10 {
		z = x * 0.25
	} else {
		z = 10*0.25 + (x-10)*0.10
	}

	fmt.Printf("Проговорил x=%.1f минут\n", x)
	fmt.Printf("Стоимость: %.2f у.е.\n", z)
	fmt.Println()

	fmt.Println("№7")
	z = 2.0

	if z <= 2.5 {
		x = z / 0.25
		if x > 10 {
			x = 10
		}
		y = 0
	} else {
		x = 10
		a = z - 2.5
		y = a / 0.10
	}

	fmt.Printf("Потратил z=%.1f у.е.\n", z)
	fmt.Printf("Минут по 0.25: %.1f\n", x)
	fmt.Printf("Минут по 0.10: %.1f\n", y)
	fmt.Println()

	fmt.Println("№8")
	a = 25.0
	b = 30.0

	x = math.Mod(a, 11)
	y = math.Mod(b, 11)
	z = x + y

	if z > 11 {
		a = a + 5
		b = b + 5
		fmt.Printf("Сумма остатков %.1f > 11\n", z)
		fmt.Printf("Новое значение: a=%.1f, b=%.1f\n", a, b)
	} else {
		fmt.Printf("Сумма остатков %.1f <= 11\n", z)
		fmt.Printf("Без изменений: a=%.1f, b=%.1f\n", a, b)
	}
	fmt.Println()

	fmt.Println("№9")
	a = 20.0
	b = 4.0

	if b != 0 {
		x = float64(int(a) / int(b))
		fmt.Printf("Целое от деления %.1f/%.1f = %.0f\n", a, b, x)

		if int(x)%2 == 0 {
			a = a * a
			b = b * b
			fmt.Printf("Четное, новыое значение: a=%.1f, b=%.1f\n", a, b)
		} else {
			fmt.Println("Нечетное, без изменений")
		}
	} else {
		fmt.Println("Деление на ноль")
	}
	fmt.Println()

	fmt.Println("№10")
	x = 4.0
	y = 5.0
	z = 6.0

	a = x + y + z
	fmt.Printf("Числа: x=%.1f, y=%.1f, z=%.1f\n", x, y, z)
	fmt.Printf("Сумма: %.1f\n", a)

	if int(a)%3 == 0 {
		b = x * y * z
		fmt.Printf("Сумма делится на 3. Произведение: %.1f\n", b)
	} else {
		fmt.Println("Сумма не делится на 3")
	}
}
