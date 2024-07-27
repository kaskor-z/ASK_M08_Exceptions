class Car:

    def __init__(self, car_model, car_vin, number):
        self.__is_valid_vin(car_vin)
        self.__is_valid_numbers(number)
        self.model = car_model
        self.__vin = car_vin
        self.__numbers = number

    def __is_valid_vin(self, vin_number):
        if not issubclass(type(vin_number), int):
            raise IncorrectVinNumber('Некорректный тип vin-номера')
            return False
        elif vin_number < 1000000 or vin_number > 9000000:
            raise IncorrectVinNumber('Неверный диапазон для vin-номера')
            return False
        else:
            return True

    def __is_valid_numbers(self, number):
        if not issubclass(type(number), str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров')
            return False
        elif len(number) != 6:
            raise IncorrectCarNumbers('Неверная длина номера')
            return False
        else:
            return True


class IncorrectVinNumber(Exception):

    def __init__(self, message):
        self.message = message


class IncorrectCarNumbers(Exception):

    def __init__(self, message):
        self.message = message


print('')
try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(exc.message)
except IncorrectCarNumbers as exc:
    print(exc.message)
else:
    print(f'{third.model} успешно создан')
