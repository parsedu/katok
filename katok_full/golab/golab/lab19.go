package main

import (
	"fmt"
	"strings"
	"unicode"
)

func main() {
	fmt.Println("\nЗадание №1")
	num1()

	fmt.Println("\nЗадание №2")
	num2()

	fmt.Println("\nЗадание №3")
	num3()

	fmt.Println("\nЗадание №4")
	num4()

	fmt.Println("\nЗадание №5")
	num5()

	fmt.Println("\nЗадание №6")
	num6()

	fmt.Println("\nЗадание №7")
	num7()

	fmt.Println("\nЗадание №8")
	num8()

	fmt.Println("\nЗадание №9")
	num9()

	fmt.Println("\nЗадание №10")
	num10()

	fmt.Println("\nЗадание №11")
	num11()

	fmt.Println("\nЗадание №12")
	num12()

	fmt.Println("\nЗадание №13")
	num13()

	fmt.Println("\nЗадание №14")
	num14()

	fmt.Println("\nЗадание №15")
	num15()
}

func num1() {
	var input string
	fmt.Print("Введите строку: ")
	fmt.Scanln(&input)

	fmt.Println("Вы ввели:", input)
}

func num2() {
	var input string
	fmt.Print("Введите строку: ")
	fmt.Scanln(&input)
	if len(input) == 0 {
		fmt.Println("Строка пустая")
		return
	}
	lastChar := input[len(input)-1]
	fmt.Printf("Последний символ: %c\n", lastChar)
}

func num3() {
	var input, substring string
	fmt.Print("Введите строку: ")
	fmt.Scanln(&input)
	fmt.Print("Введите подстроку: ")
	fmt.Scanln(&substring)

	if strings.HasSuffix(input, substring) {
		fmt.Println("Строка заканчивается подстрокой")
	} else {
		fmt.Println("Строка НЕ заканчивается подстрокой")
	}
}

func num4() {
	var input, substring string
	fmt.Print("Введите строку: ")
	fmt.Scanln(&input)
	fmt.Print("Введите подстроку: ")
	fmt.Scanln(&substring)

	if strings.HasPrefix(input, substring) {
		fmt.Println("Строка начинается с подстроки")
	} else {
		fmt.Println("Строка НЕ начинается с подстроки")
	}
}

func num5() {
	var input, substring string
	fmt.Print("Введите строку: ")
	fmt.Scanln(&input)
	fmt.Print("Введите подстроку: ")
	fmt.Scanln(&substring)

	if strings.Contains(input, substring) {
		fmt.Println("Строка содержит подстроку")
	} else {
		fmt.Println("Строка НЕ содержит подстроку")
	}
}

func num6() {
	var input, substring string
	fmt.Print("Введите строку: ")
	fmt.Scanln(&input)
	fmt.Print("Введите подстроку: ")
	fmt.Scanln(&substring)

	position := strings.Index(input, substring)
	if position != -1 {
		fmt.Printf("Подстрока найдена на позиции %d\n", position)
	} else {
		fmt.Println("Подстрока не найдена")
	}
}

func num7() {
	var text string
	fmt.Print("Введите текст: ")
	fmt.Scanln(&text)

	sent := strings.FieldsFunc(text, func(r rune) bool {
		return r == '.' || r == '!' || r == '?'
	})

	clsen := make([]string, 0)
	for _, sent := range sent {
		sent = strings.TrimSpace(sent)
		if sent != "" {
			clsen = append(clsen, sent)
		}
	}

	type SentenceInfo struct {
		text      string
		wordCount int
	}

	seninf := make([]SentenceInfo, len(clsen))
	for i, sent := range clsen {
		words := strings.Fields(sent)
		seninf[i] = SentenceInfo{
			text:      sent,
			wordCount: len(words),
		}
	}

	for i := 0; i < len(seninf)-1; i++ {
		for j := 0; j < len(seninf)-i-1; j++ {
			if seninf[j].wordCount > seninf[j+1].wordCount {
				seninf[j], seninf[j+1] = seninf[j+1], seninf[j]
			}
		}
	}

	fmt.Println("\nПредложения, упорядоченные по количеству слов:")
	for _, info := range seninf {
		fmt.Printf("Слов: %d -> %s\n", info.wordCount, info.text)
	}
}

func num8() {
	stringArray := []string{"Hello", "World"}
	fmt.Println("Строковый массив:", stringArray)

	charArray := make([]rune, 0)
	for _, str := range stringArray {
		for _, char := range str {
			charArray = append(charArray, char)
		}
	}

	fmt.Print("Символьный массив: ")
	for _, char := range charArray {
		fmt.Printf("%c ", char)
	}
	fmt.Println()
}

func num9() {
	var input string
	fmt.Print("Введите строку: ")
	fmt.Scanln(&input)

	result := strings.ReplaceAll(input, " ", "-")
	fmt.Println("Результат:", result)
}

func num10() {
	var input string
	fmt.Print("Введите строку: ")
	fmt.Scanln(&input)

	words := strings.Fields(input)
	fmt.Println("Массив слов:")
	for i, word := range words {
		fmt.Printf("%d: %s\n", i, word)
	}
}

func num11() {
	var text, letter string
	fmt.Print("Введите текст: ")
	fmt.Scanln(&text)
	fmt.Print("Введите букву: ")
	fmt.Scanln(&letter)

	if len(letter) == 0 {
		fmt.Println("Буква не введена")
		return
	}

	ralet := strings.ToLower(letter)[0]
	words := strings.Fields(text)
	result := make([]string, 0)

	for _, word := range words {
		word = strings.Trim(word, ".,!?;:")
		if len(word) > 0 && strings.ToLower(word)[0] == ralet {
			result = append(result, word)
		}
	}

	fmt.Println("Слова, начинающиеся с буквы", letter, ":")
	for i, word := range result {
		fmt.Printf("%d: %s\n", i, word)
	}
}

func num12() {
	var input string
	fmt.Print("Введите строку: ")
	fmt.Scanln(&input)

	words := strings.Fields(input)
	resw := make([]string, len(words))

	for i, word := range words {
		if len(word) > 0 {
			runes := []rune(word)
			lastIndex := len(runes) - 1
			runes[lastIndex] = unicode.ToUpper(runes[lastIndex])
			resw[i] = string(runes)
		} else {
			resw[i] = word
		}
	}

	result := strings.Join(resw, " ")
	fmt.Println("Результат:", result)
}

func num13() {
	result := "ААААААAАААА"
	fmt.Println("Сформированная строка:", result)
}

func num14() {
	var input string
	var n int

	fmt.Print("Введите строку: ")
	fmt.Scanln(&input)
	fmt.Print("Введите количество слов (n): ")
	fmt.Scan(&n)

	words := strings.Fields(input)

	if n > len(words) {
		n = len(words)
	}

	fw := words[:n]
	result := strings.Join(fw, " ")

	fmt.Printf("Первые %d слов: %s\n", n, result)
}

func num15() {
	var input string
	fmt.Print("Введите строку: ")
	fmt.Scanln(&input)

	isAllDigits := true
	for _, char := range input {
		if !unicode.IsDigit(char) {
			isAllDigits = false
			break
		}
	}

	if isAllDigits {
		fmt.Println("Строка состоит только из цифр")
	} else {
		fmt.Println("Строка содержит не только цифры")
	}
}
