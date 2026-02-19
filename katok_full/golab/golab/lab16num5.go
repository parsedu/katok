package main

import "fmt"

func sumDel(number int) int {
	if number <= 0 {
		return 0
	}

	sum := 0
	for i := 1; i <= number; i++ {
		if number%i == 0 {
			sum += i
			fmt.Println(i)
		}
	}

	return sum
}

func main() {
	var number int

	fmt.Println("Введите число:")
	fmt.Scan(&number)

	sum := sumDel(number)
	fmt.Printf("Сумма всех делителей числа %d = %d\n", number, sum)
}
