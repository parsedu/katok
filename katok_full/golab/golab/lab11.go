package main

import (
	"fmt"
	"math"
)

func main() {
	fmt.Println("\nЗадание 1")
	task1()

	fmt.Println("\nЗадание 2")
	task2()

	fmt.Println("\nЗадание 3")
	task3()

	fmt.Println("\nЗадание 4")
	task4()
	fmt.Println("\nЗадание 5")
	task5()

	fmt.Println("\nЗадание 6")
	task6()

	fmt.Println("\nЗадание 7")
	task7()

	fmt.Println("\nЗадание 8")
	task8()

	fmt.Println("\nЗадание 9")
	task9()

	fmt.Println("\nЗадание 10")
	task10()
}

func task1() {
	var n int
	fmt.Print("Размер массива: ")
	fmt.Scan(&n)

	A := make([]int, n)
	fmt.Println("Элементы массива:")
	for i := 0; i < n; i++ {
		fmt.Scan(&A[i])
	}

	fmt.Print("Массив: ")
	for i := 0; i < n; i++ {
		fmt.Print(A[i], " ")
	}
	fmt.Println()

	fn := -1
	for i := 0; i < n; i++ {
		if A[i] < 0 {
			fn = i
			break
		}
	}

	if fn == -1 {
		fmt.Println("Нет отрицательных элементов")
		return
	}

	fmt.Println("Номер первого отрицательного:", fn)

	sumNeg := 0
	for i := 0; i < n; i++ {
		if A[i] < 0 {
			sumNeg += A[i]
		}
	}
	msum := int(math.Abs(float64(sumNeg)))

	for i := fn + 1; i < n; i++ {
		if A[i] > 0 {
			A[i] += msum
		}
	}

	fmt.Print("Измененный массив: ")
	for i := 0; i < n; i++ {
		fmt.Print(A[i], " ")
	}
	fmt.Println()
}

func task2() {
	var n int
	fmt.Print("Размер массива: ")
	fmt.Scan(&n)

	A := make([]int, n)
	fmt.Println("Элементы массива:")
	for i := 0; i < n; i++ {
		fmt.Scan(&A[i])
	}

	fmt.Print("Массив: ")
	for i := 0; i < n; i++ {
		fmt.Print(A[i], " ")
	}
	fmt.Println()

	count := 0
	prod := 1

	for i := 0; i < n; i++ {
		if A[i] < 0 && count < 3 {
			prod *= A[i]
			count++
		}
	}

	if count == 0 {
		fmt.Println("Нет отрицательных элементов")
		return
	}

	if count < 3 {
		fmt.Println("Меньше трех отрицательных элементов")
		fmt.Println("Произведение найденных:", prod)
		return
	}

	fmt.Println("Произведение первых трех отрицательных:", prod)

	cha := false
	for i := 0; i < n; i++ {
		if A[i]%2 != 0 {
			A[i] = prod
			cha = true
		}
	}

	if !cha {
		fmt.Println("Нет нечетных элементов")
		return
	}

	fmt.Print("Измененный массив: ")
	for i := 0; i < n; i++ {
		fmt.Print(A[i], " ")
	}
	fmt.Println()
}

func task3() {
	var n int
	fmt.Print("Размер массива: ")
	fmt.Scan(&n)

	A := make([]int, n)
	fmt.Println("Элементы массива:")
	for i := 0; i < n; i++ {
		fmt.Scan(&A[i])
	}

	fmt.Print("Массив: ")
	for i := 0; i < n; i++ {
		fmt.Print(A[i], " ")
	}
	fmt.Println()

	max := math.MinInt64
	found := false

	for i := 1; i < n; i += 2 {
		if A[i] > max {
			max = A[i]
			found = true
		}
	}

	if !found {
		fmt.Println("Нет элементов на нечетных позициях")
		return
	}

	fmt.Println("Наибольший на нечетных позициях:", max)

	for i := 0; i < n; i += 2 {
		A[i] -= max
	}

	fmt.Print("Измененный массив: ")
	for i := 0; i < n; i++ {
		fmt.Print(A[i], " ")
	}
	fmt.Println()
}

func task4() {
	var n int
	fmt.Print("Размер массива: ")
	fmt.Scan(&n)

	A := make([]int, n)
	fmt.Println("Элементы массива:")
	for i := 0; i < n; i++ {
		fmt.Scan(&A[i])
	}

	fmt.Print("Массив: ")
	for i := 0; i < n; i++ {
		fmt.Print(A[i], " ")
	}
	fmt.Println()

	if n == 0 {
		fmt.Println("Массив пуст")
		return
	}

	max := A[0]
	min := A[0]

	for i := 1; i < n; i++ {
		if A[i] > max {
			max = A[i]
		}
		if A[i] < min {
			min = A[i]
		}
	}

	fmt.Println("Максимум:", max, "Минимум:", min)

	Sr := float64(max+min) / 2.0
	fmt.Printf("Среднее арифметическое: %.2f\n", Sr)

	for i := 0; i < n; i++ {
		if float64(A[i]) < Sr {
			A[i] = A[i] * A[i]
		}
	}

	fmt.Print("Измененный массив: ")
	for i := 0; i < n; i++ {
		fmt.Print(A[i], " ")
	}
	fmt.Println()

}
func task5() {
	var n int
	fmt.Print("Размер массива: ")
	fmt.Scan(&n)

	A := make([]int, n)
	fmt.Println("Элементы массива:")
	for i := 0; i < n; i++ {
		fmt.Scan(&A[i])
	}

	fmt.Print("Массив: ")
	for i := 0; i < n; i++ {
		fmt.Print(A[i], " ")
	}
	fmt.Println()

	min := A[0]
	max := A[0]
	for i := 1; i < n; i++ {
		if A[i] < min {
			min = A[i]
		}
		if A[i] > max {
			max = A[i]
		}
	}

	left := min / 2
	right := max / 2
	if left > right {
		left, right = right, left
	}

	fmt.Printf("Интервал: [%d, %d]\n", left, right)

	prod := 1
	found := false

	for i := 0; i < n; i++ {
		if A[i] >= left && A[i] <= right {
			prod *= A[i]
			found = true
		}
	}

	if !found {
		fmt.Println("Нет элементов в интервале")
		return
	}

	fmt.Println("Произведение элементов в интервале:", prod)

	if n >= 1 {
		A[0] = prod
	}
	if n >= 2 {
		A[n-2] = prod
	}

	fmt.Print("Измененный массив: ")
	for i := 0; i < n; i++ {
		fmt.Print(A[i], " ")
	}
	fmt.Println()
}

func task6() {
	var n int
	fmt.Print("Размер массива: ")
	fmt.Scan(&n)

	A := make([]int, n)
	fmt.Println("Элементы массива:")
	for i := 0; i < n; i++ {
		fmt.Scan(&A[i])
	}

	fmt.Print("Массив: ")
	for i := 0; i < n; i++ {
		fmt.Print(A[i], " ")
	}
	fmt.Println()

	k := 0
	for i := 0; i < n; i++ {
		if A[i]%2 == 0 {
			k++
		}
	}

	fmt.Println("Количество четных элементов:", k)

	max := A[0]
	for i := 1; i < n; i++ {
		if A[i] > max {
			max = A[i]
		}
	}

	for i := 0; i < n; i++ {
		if A[i] == max {
			A[i] = A[i] * k
			break
		}
	}

	fmt.Print("Измененный массив: ")
	for i := 0; i < n; i++ {
		fmt.Print(A[i], " ")
	}
	fmt.Println()
}

func task7() {
	var n int
	fmt.Print("Размер массива: ")
	fmt.Scan(&n)

	A := make([]int, n)
	fmt.Println("Введите элементы массива:")
	for i := 0; i < n; i++ {
		fmt.Scan(&A[i])
	}

	fmt.Print("Массив: ")
	for i := 0; i < n; i++ {
		fmt.Print(A[i], " ")
	}
	fmt.Println()

	minin := 0
	for i := 1; i < n; i++ {
		if A[i] < A[minin] {
			minin = i
		}
	}

	fmt.Println("Индекс минимального элемента:", minin)

	leftp := 1
	if minin > 0 {
		for i := 0; i < minin; i++ {
			leftp *= A[i]
		}
	} else {
		leftp = 1
	}

	rightp := 1
	if minin < n-1 {
		for i := minin + 1; i < n; i++ {
			rightp *= A[i]
		}
	} else {
		rightp = 1
	}

	totalp := leftp * rightp
	fmt.Println("Произведение элементов слева и справа от минимального:", totalp)

	minVal := A[0]
	maxVal := A[0]
	for i := 1; i < n; i++ {
		if A[i] < minVal {
			minVal = A[i]
		}
		if A[i] > maxVal {
			maxVal = A[i]
		}
	}

	if totalp != 0 {
		minVal = minVal / totalp
		maxVal = maxVal / totalp
	} else {
		fmt.Println("Произведение равно нулю, деление невозможно")
		return
	}

	fmt.Println("Минимум после деления:", minVal)
	fmt.Println("Максимум после деления:", maxVal)

	for i := 0; i < n; i++ {
		if A[i] == A[minin] {
			A[i] = minVal
		}
		if A[i] == maxVal && maxVal != minVal {
			for j := 0; j < n; j++ {
				if A[j] == maxVal && j != minin {
					A[j] = maxVal / totalp
					break
				}
			}
		}
	}

	fmt.Print("Измененный массив: ")
	for i := 0; i < n; i++ {
		fmt.Print(A[i], " ")
	}
	fmt.Println()
}

func task8() {
	var n int
	fmt.Print("Размер массива: ")
	fmt.Scan(&n)

	A := make([]int, n)
	fmt.Println("Элементы массива:")
	for i := 0; i < n; i++ {
		fmt.Scan(&A[i])
	}

	fmt.Print("Массив: ")
	for i := 0; i < n; i++ {
		fmt.Print(A[i], " ")
	}
	fmt.Println()

	minin := 0
	maxin := 0

	for i := 1; i < n; i++ {
		if A[i] < A[minin] {
			minin = i
		}
		if A[i] > A[maxin] {
			maxin = i
		}
	}

	fmt.Println("Индекс минимума:", minin, "значение:", A[minin])
	fmt.Println("Индекс максимума:", maxin, "значение:", A[maxin])

	if minin < maxin {
		fmt.Println("Минимум встречается раньше максимума")
		A[n-1] = A[maxin]
	} else {
		fmt.Println("Максимум встречается раньше минимума")
		A[0] = A[minin]
	}

	fmt.Print("Измененный массив: ")
	for i := 0; i < n; i++ {
		fmt.Print(A[i], " ")
	}
	fmt.Println()
}

func task9() {
	var n int
	fmt.Print("Размер массива: ")
	fmt.Scan(&n)

	A := make([]int, n)
	fmt.Println("Элементы массива:")
	for i := 0; i < n; i++ {
		fmt.Scan(&A[i])
	}

	fmt.Print("Массив: ")
	for i := 0; i < n; i++ {
		fmt.Print(A[i], " ")
	}
	fmt.Println()

	ordered := true
	for i := 1; i < n; i++ {
		if A[i] < A[i-1] {
			ordered = false
			break
		}
	}

	if ordered {
		fmt.Println("Массив упорядочен по возрастанию")
		A[0] = A[0] * A[0]
		A[n-1] = A[n-1] * A[n-1]
	} else {
		fmt.Println("Массив не упорядочен по возрастанию")
		A[0], A[n-1] = A[n-1], A[0]
	}

	fmt.Print("Измененный массив: ")
	for i := 0; i < n; i++ {
		fmt.Print(A[i], " ")
	}
	fmt.Println()
}

func task10() {
	var n int
	fmt.Print("Размер массива: ")
	fmt.Scan(&n)

	A := make([]int, n)
	fmt.Println("Элементы массива:")
	for i := 0; i < n; i++ {
		fmt.Scan(&A[i])
	}

	fmt.Print("Массив: ")
	for i := 0; i < n; i++ {
		fmt.Print(A[i], " ")
	}
	fmt.Println()

	ordered := true
	brokenin := -1

	for i := 1; i < n; i++ {
		if A[i] > A[i-1] {
			ordered = false
			brokenin = i
			break
		}
	}

	if ordered {
		fmt.Println("Массив упорядочен по убыванию")
		A[0] = A[0] * A[0]
		A[n-1] = A[n-1] * A[n-1]
	} else {
		fmt.Println("Массив не упорядочен по убыванию")
		fmt.Println("Индекс первого элемента, нарушающего порядок:", brokenin)

		if brokenin > 0 && brokenin < n {
			A[brokenin], A[brokenin-1] = A[brokenin-1], A[brokenin]
		}
	}

	fmt.Print("Измененный массив: ")
	for i := 0; i < n; i++ {
		fmt.Print(A[i], " ")
	}
	fmt.Println()

}
