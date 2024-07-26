


def personal_sum(numbers):
    result = 0; incorrect_data = 0
    for namber in numbers:
        try:
            result += namber
        except TypeError:
            print(f'Некорректный тип данных для подсчёта суммы - {namber}')
            incorrect_data += 1
    return result, incorrect_data

def calculate_average(numbers):
    try:
        result = personal_sum(numbers)
        average_ = result[0]/(len(numbers) - result[1])
    except ZeroDivisionError:
        average_ = 0
    except TypeError:
        print(f'В numbers записан некорректный тип данных - {type(numbers)}')
        average_ = None
    return average_

print('')
print(f'Результат 1: {calculate_average("1, 2, 3")}') # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}') # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}') # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}') # Всё должно работать
