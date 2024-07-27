class Car:

    def __init__(self, car_model, car_vin, number):
        self.__is_valid_vin(car_vin)
        self.__is_valid_numbers(number)
        self.model = car_model
        self.__vin = car_vin
        self.__numbers = number

    def __is_valid_vin(self, vin_number):
        if not issubclass(type(vin_number), int):
            raise IncorrectVinNumber('Некорректный тип vin-номера',
                                     {'vin_number = ': vin_number, 'type =': type(vin_number)})
            return False
        elif vin_number < 1000000 or vin_number > 9000000:
            raise IncorrectVinNumber('Неверный диапазон для vin-номера', {"vin_number = ": vin_number})
            return False
        else:
            return True

    def __is_valid_numbers(self, number):
        if not issubclass(type(number), str):
            raise IncorrectCarNumbers('Некорректный тип данных для номеров', {"number = ": number})
            return False
        elif len(number) != 6:
            raise IncorrectCarNumbers('Неверная длина номера', {"number = ": number})
            return False
        else:
            return True


class IncorrectVinNumber(Exception):

    def __init__(self, message, add_info):
        self.message = message
        self.add_info = add_info


class IncorrectCarNumbers(Exception):

    def __init__(self, message, add_info):
        self.message = message
        self.add_info = add_info


try:
    first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumber as exc:
    print(f' {exc.message} {exc.add_info}')
except IncorrectCarNumbers as exc:
    print(f' {exc.message} {exc.add_info}')
else:
    print(f'{first.model} успешно создан')

try:
    second = Car('Model2', 'AA300', 'т001тр')
except IncorrectVinNumber as exc:
    print(f' {exc.message} {exc.add_info}')
except IncorrectCarNumbers as exc:
    print(f' {exc.message} {exc.add_info}')
else:
    print(f'{second.model} успешно создан')

try:
    third = Car('Model2', 300, 'т001тр')
except IncorrectVinNumber as exc:
    print(f' {exc.message} {exc.add_info}')
except IncorrectCarNumbers as exc:
    print(f' {exc.message} {exc.add_info}')
else:
    print(f'{second.model} успешно создан')

try:
    fourth = Car('Model4', 1000000, 'f123djA')
except IncorrectVinNumber as exc:
    print(f' {exc.message} {exc.add_info}')
except IncorrectCarNumbers as exc:
    print(f' {exc.message} {exc.add_info}')
else:
    print(f'{first.model} успешно создан')

try:
    fifth = Car('Model5', 3000000, 123456)
except IncorrectVinNumber as exc:
    print(f' {exc.message} {exc.add_info}')
except IncorrectCarNumbers as exc:
    print(f' {exc.message} {exc.add_info}')
else:
    print(f'{second.model} успешно создан')

try:
    sixth = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumber as exc:
    print(f' {exc.message} {exc.add_info}')
except IncorrectCarNumbers as exc:
    print(f' {exc.message} {exc.add_info}')
else:
    print(f'{third.model} успешно создан')
