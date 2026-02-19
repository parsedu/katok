//go:build lab9.2
// +build lab9.2

package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

func main() {
	str := "  <-тут были пробелы->   "
	println("----------№1----------")
	println(strings.TrimSpace(str))

	println("----------№2----------")
	str2 := "Продолжаем строки изучать, ща пробелы добавим"
	probelDo := strings.Join(strings.Fields(str2), "     ")
	println(probelDo)

	println("----------№3----------")
	str3 := "<-Тут и тут пробелы будут, что бы по ширене был текст->"
	str3 = num3f(str3, 8)
	println(str3)

	println("----------№4----------")
	str4 := "капслок для текста"
	fmt.Println(strings.ToUpper(str4))

	println("----------№5----------")
	str5 := "Все слова в отдельной строке"
	num5f(str5)

	println("----------№6----------")
	str6 := "my neme is is is is"
	shift := 3
	shif := num6Shifr(str6, shift)
	fmt.Printf("Зашифрованный: %s\n", shif)

	deshift := num6Rashif(shif, shift)
	fmt.Printf("Расшифрованный: %s\n", deshift)

	println("----------№7----------")
	str7 := "однако составление алфавита утомляет"
	fmt.Println(num7f(str7))

	println("----------№8----------")
	str8 := "FF"
	pereovd, _ := strconv.ParseInt(str8, 16, 64)
	println("С 16 в 10", str8, pereovd)

	println("----------№9----------")
	str9 := "19.12.2025"
	splitanySh := strings.Split(str9, ".")

	fmt.Printf("Дата: %s\n", str9)
	fmt.Printf("День: %s\n", splitanySh[0])
	fmt.Printf("Месяц: %s\n", splitanySh[1])
	fmt.Printf("Год: %s\n", splitanySh[2])

	println("----------№10----------")

	vbod := bufio.NewReader(os.Stdin)
	fmt.Println("Введите предложение:")
	inp, _ := vbod.ReadString('\n')

	inp = strings.TrimSpace(inp)
	charCount := len([]rune(inp))
	words := strings.Fields(inp)
	worCou := len(words)
	var shor, long string

	if worCou > 0 {
		shor = words[0]
		long = words[0]

		for _, word := range words {
			if len(word) < len(shor) {
				shor = word
			}
			if len(word) > len(long) {
				long = word
			}
		}
	}
	fmt.Printf("Кол-во символов: %d\n", charCount)
	fmt.Printf("Кол-во слов: %d\n", worCou)
	if worCou > 0 {
		fmt.Printf("Самое короткое: \"%s\" (%d символов)\n", shor, len(shor))
		fmt.Printf("Самое длинное: \"%s\" (%d символов)\n", long, len(long))
	} else {
		fmt.Println("В предложении нет слов")
	}

	println("----------№11----------")
	str11 := "<-тут пробелы будут"
	str11 = num11f(str11, 8)
	println(str11)

	println("----------№12----------")
	str12 := "  два пробела   три пробела      пять пробелов"
	fmt.Println(num12f(str12))

	println("----------№13----------")
	str13 := "моя попытка номер пять"
	vol := "аеёиоуыэюяaeiou"
	volCount := 0
	consCount := 0

	for _, char := range str13 {
		if char >= 'а' && char <= 'я' || char == 'ё' || char >= 'a' && char <= 'z' {
			if strings.ContainsRune(vol, char) {
				volCount++
			} else {
				consCount++
			}
		}
	}
	fmt.Printf("Гласных: %d\n", volCount)
	fmt.Printf("Согласных: %d\n", consCount)

	println("----------№14----------")

	read := bufio.NewReader(os.Stdin)
	fmt.Print("Введите текст: ")
	text, _ := read.ReadString('\n')
	text = strings.TrimSpace(text)

	fmt.Println("\n как сделать?:")
	fmt.Println("1 - По левому краю")
	fmt.Println("2 - По правому краю")
	fmt.Println("3 - По центру")
	fmt.Println("4 - По ширине")

	choInp, _ := read.ReadString('\n')
	choInp = strings.TrimSpace(choInp)
	ch, _ := strconv.Atoi(choInp)
	width := 50
	result := num14f(text, width, ch)
	fmt.Println(result)

	println("----------№15----------")
	var a, b, c float64

	fmt.Print("Введите сторону a: ")
	fmt.Scanln(&a)
	fmt.Print("Введите сторону b: ")
	fmt.Scanln(&b)
	fmt.Print("Введите сторону c: ")
	fmt.Scanln(&c)

	if a+b > c && a+c > b && b+c > a {
		fmt.Println("Треугольник существует")
		if a == b && b == c {
			fmt.Println("Треугольник равносторонний")
		} else {
			fmt.Println("Треугольник не равносторонний")
		}
	} else {
		fmt.Println("Треугольник не существует")
	}

	println("----------№16----------")
	var x1, y1, x2, y2, x3, y3 float64
	fmt.Print("Введите сторону x1: ")
	fmt.Scanln(&x1)
	fmt.Print("Введите сторону y1: ")
	fmt.Scanln(&y1)
	fmt.Print("Введите сторону x2: ")
	fmt.Scanln(&x2)
	fmt.Print("Введите сторону y2: ")
	fmt.Scanln(&y2)
	fmt.Print("Введите сторону x3: ")
	fmt.Scanln(&x3)
	fmt.Print("Введите сторону y3: ")
	fmt.Scanln(&y3)

	x4 := x1 + x3 - x2
	y4 := y1 + y3 - y2
	fmt.Printf("Координаты четвертой вершины: (%.2f, %.2f)\n", x4, y4)
}

func num5f(str string) {
	words := strings.Fields(str)
	for _, word := range words {
		fmt.Println(word)
	}
}

func num3f(input string, ind int) string {
	spaces := strings.Repeat(" ", ind)
	return spaces + input + spaces
}

func num11f(input string, ind int) string {
	ped := ind + len(input)
	return fmt.Sprintf("% "+strconv.Itoa(ped)+"s", input)
}

var translit = map[rune]string{
	'а': "a", 'б': "b", 'в': "v", 'г': "g", 'д': "d",
	'е': "e", 'ё': "yo", 'ж': "zh", 'з': "z", 'и': "i",
	'й': "y", 'к': "k", 'л': "l", 'м': "m", 'н': "n",
	'о': "o", 'п': "p", 'р': "r", 'с': "s", 'т': "t",
	'у': "u", 'ф': "f", 'х': "kh", 'ц': "ts", 'ч': "ch",
	'ш': "sh", 'щ': "shch", 'ъ': "", 'ы': "y", 'ь': "",
	'э': "e", 'ю': "yu", 'я': "ya",
	'А': "A", 'Б': "B", 'В': "V", 'Г': "G", 'Д': "D",
	'Е': "E", 'Ё': "Yo", 'Ж': "Zh", 'З': "Z", 'И': "I",
	'Й': "Y", 'К': "K", 'Л': "L", 'М': "M", 'Н': "N",
	'О': "O", 'П': "P", 'Р': "R", 'С': "S", 'Т': "T",
	'У': "U", 'Ф': "F", 'Х': "Kh", 'Ц': "Ts", 'Ч': "Ch",
	'Ш': "Sh", 'Щ': "Shch", 'Ъ': "", 'Ы': "Y", 'Ь': "'",
	'Э': "E", 'Ю': "Yu", 'Я': "Ya",
}

func num7f(text string) string {
	var result strings.Builder

	for _, char := range text {
		if per, ok := translit[char]; ok {
			result.WriteString(per)
		} else {
			result.WriteRune(char)
		}
	}

	return result.String()
}
func num6Shifr(text string, shift int) string {
	result := ""

	for _, char := range text {
		if char >= 'a' && char <= 'z' {
			newChar := 'a' + (char-'a'+rune(shift))%26
			result += string(newChar)
		} else if char >= 'A' && char <= 'Z' {

			newChar := 'A' + (char-'A'+rune(shift))%26
			result += string(newChar)
		} else {

			result += string(char)
		}
	}

	return result
}

func num6Rashif(text string, shift int) string {
	return num6Shifr(text, 26-shift)
}

func num12f(input string) string {
	words := strings.Fields(input)
	return strings.Join(words, " ")
}

func num14f(text string, width int, mode int) string {
	text = strings.TrimSpace(text)
	leng := len([]rune(text))

	if leng >= width {
		return string([]rune(text)[:width])
	}

	sp := width - leng

	switch mode {
	case 1:
		return text + strings.Repeat(" ", sp)
	case 2:
		return strings.Repeat(" ", sp) + text
	case 3:
		left := sp / 2
		return strings.Repeat(" ", left) + text + strings.Repeat(" ", sp-left)
	case 4:
		words := strings.Fields(text)
		if len(words) < 2 {
			return text + strings.Repeat(" ", sp)
		}

		woLn := 0
		for _, w := range words {
			woLn += len([]rune(w))
		}

		ne := width - woLn
		ga := len(words) - 1
		ba := ne / ga
		ex := ne % ga

		resu := words[0]
		for i := 1; i < len(words); i++ {
			sp := ba
			if i <= ex {
				sp++
			}
			resu += strings.Repeat(" ", sp+1) + words[i]
		}
		return resu
	}

	return text
}
