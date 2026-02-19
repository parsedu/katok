package main

import "fmt"

func remNum(arr []int) ([]int, []int) {
	if len(arr) == 0 {
		return []int{}, []int{}
	}

	result := []int{arr[0]}
	removed := []int{}

	for i := 1; i < len(arr); i++ {
		if arr[i] != arr[i-1] {
			result = append(result, arr[i])
		} else {
			removed = append(removed, arr[i])
		}
	}

	return result, removed
}

func main() {
	arr := []int{1, 2, 2, 3, 4, 4, 4, 5, 5, 6}

	cleaned, removed := remNum(arr)

	fmt.Printf("Исходный массив: %v\n", arr)
	fmt.Printf("Очищенный массив: %v\n", cleaned)
	fmt.Printf("Удаленные элементы: %v\n", removed)
}
