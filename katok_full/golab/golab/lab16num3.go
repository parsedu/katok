package main

import "fmt"

func main() {
	fmt.Println("Введите количество секун:")

	for {
		var sec int64
		fmt.Print("> ")
		fmt.Scan(&sec)

		if sec == 0 {
			break
		}

		days := sec / 86400
		remainder := sec % 86400
		hours := remainder / 3600
		minutes := (remainder % 3600) / 60
		seconds := remainder % 60

		fmt.Printf("%d сек = %d суток ", sec, days)
		fmt.Printf("(%d:%02d:%02d)\n\n", hours, minutes, seconds)
	}
}
