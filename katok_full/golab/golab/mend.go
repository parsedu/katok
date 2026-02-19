package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"strings"
)

type Element struct {
	Number       int
	Symbol       string
	Name         string
	State        string
	AtomicWeight float64
}

type MendeleevTable struct {
	elements []Element
}

func NewMendeleevTable() *MendeleevTable {
	mt := &MendeleevTable{
		elements: make([]Element, 0),
	}

	mt.fillWithElements()

	return mt
}

func (mt *MendeleevTable) fillWithElements() {
	elements := []Element{
		{1, "H", "водород", "газ", 1.008},
		{2, "He", "гелий", "газ", 4.0026},
		{3, "Li", "литий", "металл", 6.941},
		{4, "Be", "бериллий", "металл", 9.012},
		{5, "B", "бор", "твердый", 10.811},
		{6, "C", "углерод", "твердый", 12.011},
		{7, "N", "азот", "газ", 14.007},
		{8, "O", "кислород", "газ", 15.999},
		{9, "F", "фтор", "газ", 18.998},
		{10, "Ne", "неон", "газ", 20.180},
		{11, "Na", "натрий", "металл", 22.990},
		{12, "Mg", "магний", "металл", 24.305},
		{13, "Al", "алюминий", "металл", 26.982},
		{14, "Si", "кремний", "твердый", 28.086},
		{15, "P", "фосфор", "твердый", 30.974},
		{16, "S", "сера", "твердый", 32.065},
		{17, "Cl", "хлор", "газ", 35.453},
		{18, "Ar", "аргон", "газ", 39.948},
		{19, "K", "калий", "металл", 39.098},
		{20, "Ca", "кальций", "металл", 40.078},

		{22, "Ti", "титан", "металл", 47.867},
		{24, "Cr", "хром", "металл", 51.996},
		{25, "Mn", "марганец", "металл", 54.938},
		{26, "Fe", "железо", "металл", 55.845},
		{27, "Co", "кобальт", "металл", 58.933},
		{28, "Ni", "никель", "металл", 58.693},
		{29, "Cu", "медь", "металл", 63.546},
		{30, "Zn", "цинк", "металл", 65.380},

		{33, "As", "мышьяк", "твердый", 74.922},
		{35, "Br", "бром", "жидкость", 79.904},
		{47, "Ag", "серебро", "металл", 107.87},
		{50, "Sn", "олово", "металл", 118.710},
		{53, "I", "йод", "твердый", 126.90},
		{79, "Au", "золото", "металл", 196.97},
		{80, "Hg", "ртуть", "жидкость", 200.59},
		{82, "Pb", "свинец", "металл", 207.2},
		{92, "U", "уран", "металл", 238.03},
	}

	mt.elements = append(mt.elements, elements...)
}

func (mt *MendeleevTable) AddElement(element Element) {
	mt.elements = append(mt.elements, element)
}

func (mt *MendeleevTable) FindByNumber(number int) *Element {
	for i := range mt.elements {
		if mt.elements[i].Number == number {
			return &mt.elements[i]
		}
	}
	return nil
}

func (mt *MendeleevTable) FindBySymbol(symbol string) *Element {
	for i := range mt.elements {
		if strings.EqualFold(mt.elements[i].Symbol, symbol) {
			return &mt.elements[i]
		}
	}
	return nil
}

func (mt *MendeleevTable) FindByName(name string) *Element {
	for i := range mt.elements {
		if strings.Contains(strings.ToLower(mt.elements[i].Name), strings.ToLower(name)) {
			return &mt.elements[i]
		}
	}
	return nil
}

func (mt *MendeleevTable) UpdateElement(number int, newElement Element) bool {
	for i := range mt.elements {
		if mt.elements[i].Number == number {
			mt.elements[i] = newElement
			return true
		}
	}
	return false
}

func (mt *MendeleevTable) DeleteElement(number int) bool {
	for i := range mt.elements {
		if mt.elements[i].Number == number {
			mt.elements = append(mt.elements[:i], mt.elements[i+1:]...)
			return true
		}
	}
	return false
}

func (mt *MendeleevTable) SortByNumber() {
	sort.Slice(mt.elements, func(i, j int) bool {
		return mt.elements[i].Number < mt.elements[j].Number
	})
}

func (mt *MendeleevTable) SortByName() {
	sort.Slice(mt.elements, func(i, j int) bool {
		return strings.ToLower(mt.elements[i].Name) < strings.ToLower(mt.elements[j].Name)
	})
}

func (mt *MendeleevTable) SortByWeight() {
	sort.Slice(mt.elements, func(i, j int) bool {
		return mt.elements[i].AtomicWeight < mt.elements[j].AtomicWeight
	})
}

func (mt *MendeleevTable) GetAllElements() []Element {
	return mt.elements
}

func (mt *MendeleevTable) GetCount() int {
	return len(mt.elements)
}

func (mt *MendeleevTable) InputElement() Element {
	reader := bufio.NewReader(os.Stdin)
	var element Element

	fmt.Println("\n" + strings.Repeat("=", 50))
	fmt.Println("              ВВОД НОВОГО ЭЛЕМЕНТА")
	fmt.Println(strings.Repeat("=", 50))

	for {
		fmt.Print("Номер элемента: ")
		numStr, _ := reader.ReadString('\n')
		numStr = strings.TrimSpace(numStr)
		num, err := strconv.Atoi(numStr)

		if err != nil {
			fmt.Println("Ошибка: введите целое число!")
			continue
		}

		if mt.FindByNumber(num) != nil {
			fmt.Printf("Элемент с номером %d уже существует!\n", num)
			continue
		}

		element.Number = num
		break
	}

	fmt.Print("Символ (например, Fe): ")
	symbol, _ := reader.ReadString('\n')
	element.Symbol = strings.TrimSpace(symbol)

	fmt.Print("Название (например, железо): ")
	name, _ := reader.ReadString('\n')
	element.Name = strings.TrimSpace(name)

	fmt.Print("Агрегатное состояние (газ, жидкость, твердый, металл): ")
	state, _ := reader.ReadString('\n')
	element.State = strings.TrimSpace(state)

	for {
		fmt.Print("Атомарный вес (например, 55.84): ")
		weightStr, _ := reader.ReadString('\n')
		weightStr = strings.TrimSpace(weightStr)
		weight, err := strconv.ParseFloat(weightStr, 64)

		if err != nil {
			fmt.Println("Ошибка: введите число!")
			continue
		}

		element.AtomicWeight = weight
		break
	}

	fmt.Println("\n✓ Элемент успешно добавлен!")
	return element
}

func (mt *MendeleevTable) PrintElement(element Element) {
	fmt.Printf("\n%3d | %-3s | %-20s | %-12s | %7.2f\n",
		element.Number,
		element.Symbol,
		element.Name,
		element.State,
		element.AtomicWeight)
}

func (mt *MendeleevTable) PrintElementDetailed(element Element) {
	fmt.Println("\n" + strings.Repeat("=", 50))
	fmt.Println("              ИНФОРМАЦИЯ ОБ ЭЛЕМЕНТАХ")
	fmt.Println(strings.Repeat("=", 50))

	fmt.Printf("Номер:           %d\n", element.Number)
	fmt.Printf("Символ:          %s\n", element.Symbol)
	fmt.Printf("Название:        %s\n", element.Name)
	fmt.Printf("Состояние:       %s\n", element.State)
	fmt.Printf("Атомарный вес:   %.2f\n", element.AtomicWeight)

	fmt.Println(strings.Repeat("=", 50))
}

func (mt *MendeleevTable) ShowAllElements() {
	elements := mt.GetAllElements()

	if len(elements) == 0 {
		fmt.Println("\nТаблица пуста!")
		return
	}

	fmt.Println("\n" + strings.Repeat("=", 70))
	fmt.Println("                    ТАБЛИЦА МЕНДЕЛЕЕВА")
	fmt.Println(strings.Repeat("=", 70))
	fmt.Printf("%4s | %-4s | %-20s | %-15s | %10s\n",
		"№", "Симв", "Название", "Состояние", "Вес")
	fmt.Println(strings.Repeat("-", 70))

	for _, element := range elements {
		fmt.Printf("%4d | %-4s | %-20s | %-15s | %10.2f\n",
			element.Number,
			element.Symbol,
			element.Name,
			element.State,
			element.AtomicWeight)
	}

	fmt.Println(strings.Repeat("=", 70))
	fmt.Printf("Всего элементов: %d\n", len(elements))
}

func (mt *MendeleevTable) SearchMenu() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Println("\n" + strings.Repeat("=", 50))
	fmt.Println("Поиск элемента")
	fmt.Println(strings.Repeat("=", 50))
	fmt.Println("1. По номеру")
	fmt.Println("2. По символу")
	fmt.Println("3. По названию")
	fmt.Println("0. Назад")
	fmt.Println(strings.Repeat("-", 50))

	fmt.Print("Выберите действие: ")
	choiceStr, _ := reader.ReadString('\n')
	choiceStr = strings.TrimSpace(choiceStr)
	choice, err := strconv.Atoi(choiceStr)

	if err != nil {
		fmt.Println("Ошибка ввода!")
		return
	}

	var found *Element

	switch choice {
	case 1:
		fmt.Print("Введите номер элемента: ")
		numStr, _ := reader.ReadString('\n')
		numStr = strings.TrimSpace(numStr)
		num, err := strconv.Atoi(numStr)

		if err != nil {
			fmt.Println("Ошибка: введите целое число!")
			return
		}

		found = mt.FindByNumber(num)

	case 2:
		fmt.Print("Введите символ элемента: ")
		symbol, _ := reader.ReadString('\n')
		symbol = strings.TrimSpace(symbol)
		found = mt.FindBySymbol(symbol)

	case 3:
		fmt.Print("Введите название элемента: ")
		name, _ := reader.ReadString('\n')
		name = strings.TrimSpace(name)
		found = mt.FindByName(name)

	case 0:
		return

	default:
		fmt.Println("Неверный выбор!")
		return
	}

	if found != nil {
		mt.PrintElementDetailed(*found)
	} else {
		fmt.Println("Элемент не найден!")
	}
}

func (mt *MendeleevTable) EditMenu() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Println("\n" + strings.Repeat("=", 50))
	fmt.Println("Редактирование")
	fmt.Println(strings.Repeat("=", 50))

	fmt.Print("Введите номер элемента для редактирования: ")
	numStr, _ := reader.ReadString('\n')
	numStr = strings.TrimSpace(numStr)
	number, err := strconv.Atoi(numStr)

	if err != nil {
		fmt.Println("Ошибка: введите целое число!")
		return
	}

	element := mt.FindByNumber(number)
	if element == nil {
		fmt.Println("Элемент не найден!")
		return
	}

	fmt.Println("\nТекущие данные:")
	mt.PrintElementDetailed(*element)

	var newElement Element
	newElement.Number = element.Number

	fmt.Print("\nНовый символ (оставьте пустым, чтобы не менять): ")
	newSymbol, _ := reader.ReadString('\n')
	newSymbol = strings.TrimSpace(newSymbol)
	if newSymbol != "" {
		newElement.Symbol = newSymbol
	} else {
		newElement.Symbol = element.Symbol
	}

	fmt.Print("Новое название (оставьте пустым, чтобы не менять): ")
	newName, _ := reader.ReadString('\n')
	newName = strings.TrimSpace(newName)
	if newName != "" {
		newElement.Name = newName
	} else {
		newElement.Name = element.Name
	}

	fmt.Print("Новое состояние (оставьте пустым, чтобы не менять): ")
	newState, _ := reader.ReadString('\n')
	newState = strings.TrimSpace(newState)
	if newState != "" {
		newElement.State = newState
	} else {
		newElement.State = element.State
	}

	fmt.Print("Новый атомарный вес (введите 0, чтобы не менять): ")
	weightStr, _ := reader.ReadString('\n')
	weightStr = strings.TrimSpace(weightStr)
	newWeight, err := strconv.ParseFloat(weightStr, 64)

	if err == nil && newWeight > 0 {
		newElement.AtomicWeight = newWeight
	} else {
		newElement.AtomicWeight = element.AtomicWeight
	}

	mt.UpdateElement(number, newElement)
	fmt.Println("\n✓ Элемент успешно обновлен!")
}

func (mt *MendeleevTable) DeleteMenu() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Println("\n" + strings.Repeat("=", 50))
	fmt.Println("                  УДАЛЕНИЕ ЭЛЕМЕНТА")
	fmt.Println(strings.Repeat("=", 50))

	fmt.Print("Введите номер элемента для удаления: ")
	numStr, _ := reader.ReadString('\n')
	numStr = strings.TrimSpace(numStr)
	number, err := strconv.Atoi(numStr)

	if err != nil {
		fmt.Println("Ошибка: введите целое число!")
		return
	}

	element := mt.FindByNumber(number)
	if element == nil {
		fmt.Println("Элемент не найден!")
		return
	}

	fmt.Print("\nВы уверены? (да/нет): ")
	confirm, _ := reader.ReadString('\n')
	confirm = strings.TrimSpace(strings.ToLower(confirm))

	if confirm == "да" || confirm == "д" || confirm == "y" || confirm == "yes" {
		if mt.DeleteElement(number) {
			fmt.Println("✓ Элемент успешно удален!")
		} else {
			fmt.Println("Ошибка при удалении элемента!")
		}
	} else {
		fmt.Println("Удаление отменено.")
	}
}

func (mt *MendeleevTable) SortMenu() {
	reader := bufio.NewReader(os.Stdin)

	fmt.Println("\n" + strings.Repeat("=", 50))
	fmt.Println("СОРТИРОВКА ЭЛЕМЕНТОВ")
	fmt.Println(strings.Repeat("=", 50))
	fmt.Println("1. По номеру (по возрастанию)")
	fmt.Println("2. По названию (по алфавиту)")
	fmt.Println("3. По атомарному весу (по возрастанию)")
	fmt.Println("0. Назад")
	fmt.Println(strings.Repeat("-", 50))

	fmt.Print("Выберите способ сортировки: ")
	choiceStr, _ := reader.ReadString('\n')
	choiceStr = strings.TrimSpace(choiceStr)
	choice, err := strconv.Atoi(choiceStr)

	if err != nil {
		fmt.Println("Ошибка ввода!")
		return
	}

	switch choice {
	case 1:
		mt.SortByNumber()
		fmt.Println("\n✓ Элементы отсортированы по номеру")
		mt.ShowAllElements()

	case 2:
		mt.SortByName()
		fmt.Println("\n✓ Элементы отсортированы по названию")
		mt.ShowAllElements()

	case 3:
		mt.SortByWeight()
		fmt.Println("\n✓ Элементы отсортированы по атомарному весу")
		mt.ShowAllElements()

	case 0:
		return

	default:
		fmt.Println("Неверный выбор!")
	}
}

func (mt *MendeleevTable) ShowStatistics() {
	elements := mt.GetAllElements()

	if len(elements) == 0 {
		fmt.Println("\nТаблица пуста!")
		return
	}

	fmt.Println("\n" + strings.Repeat("=", 50))
	fmt.Println("                 СТАТИСТИКА")
	fmt.Println(strings.Repeat("=", 50))

	fmt.Printf("Всего элементов: %d\n", len(elements))

	stateCount := make(map[string]int)
	totalWeight := 0.0

	for _, element := range elements {
		stateCount[element.State]++
		totalWeight += element.AtomicWeight
	}

	fmt.Printf("Средний атомарный вес: %.2f\n", totalWeight/float64(len(elements)))

	fmt.Println("\nРаспределение по состояниям:")
	for state, count := range stateCount {
		fmt.Printf("  %-10s: %d элементов\n", state, count)
	}

	if len(elements) > 0 {
		lightest := elements[0]
		heaviest := elements[0]

		for _, element := range elements {
			if element.AtomicWeight < lightest.AtomicWeight {
				lightest = element
			}
			if element.AtomicWeight > heaviest.AtomicWeight {
				heaviest = element
			}
		}

		fmt.Println("\nСамый легкий элемент:")
		fmt.Printf("  %s (%s) - %.2f\n", lightest.Name, lightest.Symbol, lightest.AtomicWeight)

		fmt.Println("Самый тяжелый элемент:")
		fmt.Printf("  %s (%s) - %.2f\n", heaviest.Name, heaviest.Symbol, heaviest.AtomicWeight)
	}

	fmt.Println(strings.Repeat("=", 50))
}

func (mt *MendeleevTable) ShowMenu() {
	reader := bufio.NewReader(os.Stdin)

	for {
		fmt.Println("\n" + strings.Repeat("=", 60))
		fmt.Println(strings.Repeat("=", 60))
		fmt.Printf("Элементов в таблице: %d\n", mt.GetCount())
		fmt.Println(strings.Repeat("-", 60))
		fmt.Println("1. Добавить новый элемент")
		fmt.Println("2. Показать все элементы")
		fmt.Println("3. Поиск элемента")
		fmt.Println("4. Редактировать элемент")
		fmt.Println("5. Удалить элемент")
		fmt.Println("6. Сортировка элементов")
		fmt.Println("7. Статистика")
		fmt.Println("0. Выход")
		fmt.Println(strings.Repeat("=", 60))

		fmt.Print("Выберите действие: ")
		choiceStr, _ := reader.ReadString('\n')
		choiceStr = strings.TrimSpace(choiceStr)
		choice, err := strconv.Atoi(choiceStr)

		if err != nil {
			fmt.Println("Ошибка ввода! Введите число.")
			continue
		}

		switch choice {
		case 1:
			element := mt.InputElement()
			mt.AddElement(element)

		case 2:
			mt.ShowAllElements()

		case 3:
			mt.SearchMenu()

		case 4:
			mt.EditMenu()

		case 5:
			mt.DeleteMenu()

		case 6:
			mt.SortMenu()

		case 7:
			mt.ShowStatistics()

		case 0:
			fmt.Println("\nДо свидания!")
			return

		default:
			fmt.Println("Неверный выбор! Попробуйте снова.")
		}
		fmt.Print("\nНажмите Enter для продолжения...")
		reader.ReadString('\n')
	}
}

func main() {
	table := NewMendeleevTable()
	fmt.Printf("Таблица уже содержит %d элементов!\n", table.GetCount())
	table.ShowMenu()
}
