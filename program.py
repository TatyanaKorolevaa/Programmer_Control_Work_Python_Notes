import personal_notes


def create_note(number):
    title = check_len_text_input(
        input('Введите Название заметки: '), number)
    body = check_len_text_input(
        input('Введите Описание заметки: '), number)
    return personal_notes.personal_notes(title=title, body=body)


def menu():
    print("\nВыберите действие:\n\n1 - Все заметки\n2 - Создание заметки\n3 - Удаление заметки\n4 - Редактирование заметки\n5 - Выбор заметки по дате\n6 - Выбор заметки по id\n7 - Выход\n\nВведите номер функции: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите тескт: ')
    else:
        return text
