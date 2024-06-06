# Lab-1
Лабораторна робота 1
Мета роботи
Мета цієї лабораторної роботи - ознайомлення з основами програмування на Python. Очікувані результати включають вивчення базових операцій з рядками, виконання математичних операцій та роботу з колекціями даних.

Опис завдання
Завдання 1: Написати функцію, яка приймає рядок і повертає його довжину.
Завдання 2: Написати функцію, яка виконує основні арифметичні операції (+, -, *, /, //, **) між двома числами.
Завдання 3: Написати функцію, яка знаходить максимальне число у списку чисел.
Виконання роботи
Крок 1: Реалізувати функцію task1, яка визначає довжину переданого рядка.
def task1(string):
    return len(string)
    
Приклад використання:
input_string = "Це тестовий рядок"
length = task1(input_string)
print("Довжина рядка:", length)


Крок 2: Реалізувати функцію task2, яка виконує задану арифметичну операцію між двома числами.
def task2(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '/':
        return num1 / num2
    elif operator == '//':
        return num1 // num2
    elif operator == '**':
        return num1 ** num2
    elif operator == '*':
        return num1 * num2
    else:
        return "Неправильна операція"
        
Приклад використання:
number1 = 10
number2 = 5
operation = '*'
result = task2(number1, operation, number2)
print(f"{number1} {operation} {number2} = {result}")
Крок 3: Реалізувати функцію task3, яка знаходить максимальне число у списку.
def task3(numbers):
    if not numbers:
        return None  
    max_value = numbers[0]  
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value
    
Приклад використання:
number_list = [10, 5, 8, 20, 15]
max_number = task3(number_list)
print("Максимальне число у списку:", max_number)

Приклади виводу програми:

Довжина рядка: 16
10 * 5 = 50
Максимальне число у списку: 20


Інструкції з запуску

Вимоги до середовища: Python 3.x
