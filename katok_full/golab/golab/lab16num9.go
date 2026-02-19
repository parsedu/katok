package main

import "fmt"

func minMax(arr []int) []int {
	if len(arr) == 0 {
		return []int{}
	}

	min := arr[0]
	max := arr[0]

	for i := 1; i < len(arr); i++ {
		if arr[i] < min {
			min = arr[i]
		}
		if arr[i] > max {
			max = arr[i]
		}
	}

	return []int{max, min}
}

func main() {
	tArr := [][]int{
		{5, 3, 8, 1, 9, 2},
		{10, 10, 10, 10},
		{-5, -1, -8, -3},
		{0, 100, -50, 25},
	}

	for _, arr := range tArr {
		result := minMax(arr)
		fmt.Printf("%d, %d\n", result[0], result[1])
	}
}
