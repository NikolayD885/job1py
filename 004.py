# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
# Пример: - 6 -> да
#         - 7 -> да
#         - 1 -> нет

Number = int(input('Введите цифру дня недели: '))

match Number:

    case 1:
        print('Рабочий день')
    case 2:
        print('Рабочий день')
    case 3:
        print('Рабочий день')
    case 4:
        print('Рабочий день')
    case 5:
        print('Рабочий день')
    case 6:
        print('Суббота')
    case 7:
        print('Воскресенье')
    case _:
        print('Не является днем недели')