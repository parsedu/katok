package main

import "fmt"

func Zodiac(day, month int) string {
	signs := []ZodiacSign{
		{"Козерог", 1, 20},
		{"Водолей", 2, 19},
		{"Рыбы", 3, 20},
		{"Овен", 4, 20},
		{"Телец", 5, 21},
		{"Близнецы", 6, 21},
		{"Рак", 7, 22},
		{"Лев", 8, 23},
		{"Дева", 9, 23},
		{"Весы", 10, 23},
		{"Скорпион", 11, 22},
		{"Стрелец", 12, 21},
		{"Козерог", 12, 31},
	}

	if month < 1 || month > 12 || day < 1 || day > 31 {
		return "Неверная дата"
	}

	for i, sign := range signs {
		if month == sign.Month {
			if day <= sign.DayMax {
				return sign.Name
			}

			if i+1 < len(signs) {
				return signs[i+1].Name
			}
		}
	}

	return "Неизвестный знак"
}

func main() {
	var day, month int
	fmt.Print("День рождения: ")
	fmt.Scan(&day)

	fmt.Print("Месяц рождения: ")
	fmt.Scan(&month)

	sign := Zodiac(day, month)
	fmt.Printf("\nЗнак зодиака: %s\n", sign)
}

type ZodiacSign struct {
	Name   string
	Month  int
	DayMax int
}
