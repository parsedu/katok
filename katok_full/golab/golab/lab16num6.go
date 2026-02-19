package main

import "fmt"

func Dump(arr []int) []int {
	if len(arr) == 0 {
		return []int{}
	}

	temp := make([]int, len(arr))
	count := 0

	for i := 0; i < len(arr); i++ {
		found := false

		for j := 0; j < count; j++ {
			if arr[i] == temp[j] {
				found = true
				break
			}
		}

		if !found {
			temp[count] = arr[i]
			count++
		}
	}

	result := make([]int, count)
	copy(result, temp[:count])

	return result
}

func main() {
	arr := []int{1, 2, 2, 3, 4, 4, 5, 1, 3, 5}
	fmt.Println("Исходный массив:", arr)
	fmt.Println("Без дубликатов:", Dump(arr))
}
