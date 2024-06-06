def task1(string):
    return len(string)


input_string = "Це тестовий рядок"
length = task1(input_string)
print("Довжина рядка:", length)


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


number1 = 10
number2 = 5
operation = '*'
result = task2(number1, operation, number2)
print(f"{number1} {operation} {number2} = {result}")


def task3(numbers):
    if not numbers:
        return None  
    max_value = numbers[0]  
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value


number_list = [10, 5, 8, 20, 15]
max_number = task3(number_list)
print("Максимальне число у списку:", max_number)
