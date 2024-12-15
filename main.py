
"""
Главный модуль программы
Осуществляет выполнение выбранной из меню задачи, посредством вызова
соответствующей подпрограммы
Перед вызовом запрашивает нужные исходные данные подпрограммы
"""

from lab5.my_library import task5_1, task5_2, task5_3, task5_4, task5_5, task5_6, task5_7


def menu():
    """
    Функция предлагает выбор номера задания\n
    :param : нет передаваемых параметров
    :return: choice_task - выбранный номер задания
    """

    choice_task = int(input('Выберите номер задания в лабораторной работе: '))

    return choice_task

if __name__ == '__main__':
    while True:
        choice = menu()

        match choice:

            case 1:
            # Ввод строки
                s = input('Введите строку: ')
                positions_chu, positions_shu = task5_1(s)

                if positions_chu:
                    print(f"Буквосочетание 'чу' найдено на позициях: {positions_chu}")
                else:
                    print("Буквосочетание 'чу' не найдено.")

                if positions_shu:
                    print(f"Буквосочетание 'щу' найдено на позициях: {positions_shu}")
                else:
                    print("Буквосочетание 'щу' не найдено.")



            case 2:
                text = input('Введите текст: ')
                print(task5_2(text))

            case 3:
                text = input("Введите строку: ")
                symbol = input("Введите символ для удаления: ")
                flag = int(input("Введите флаг (0 - удалить, 1 - вставить): "))
                task5_3(text, symbol, flag)

            case 4:
                text = input('Введите текст на английском языке: ')
                print(task5_4(text))

            case 5:
                ticket_number = input("Введите номер билета: ")
                task5_5(ticket_number)

            case 6:
                s = input('Введите строку: ')
                task5_6(s)

            case 7:
                text = input("Введите текст: ")
                print(task5_7(text))

            case _:
                    break
        if input('Продолжить? Да/Нет: ') == 'Нет'.lower(): break

