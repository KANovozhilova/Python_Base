"""
Задача 4: Пользователь вводит целое положительное число.
Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""

# через последовательное сравнение элементов от 1 до последнего в числе
input_number = input("Введите целое положительное число: ")
number_lenght = len(input_number)
max_element = 0
i = 0
while i < number_lenght:
    current_element = int(input_number[i])
    if current_element > max_element:
        max_element = current_element
    i += 1
print(max_element)


# через последовательное отсечение последнего элемента от числа
input_number = int(input_number)
max_element = 0
while input_number != 0:
    last_element = input_number % 10
    input_number = input_number//10
    if last_element > max_element:
        max_element = last_element
print(max_element)


# через перевод числа в лист и выделение максимального числа
input_numbers = list(input_number)
print(max(input_numbers))


# без использования while и арифметических операций
max_element = 0
for element in input_number:
    if int(element) > max_element:
        max_element = int(element)
print(max_element)




