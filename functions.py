import file_action
import personal_notes
import program

number = 5  # сколько знаков МИНИМУМ может быть в тексте заметки


def add():
    note = program.create_note(number)
    array = file_action.read_file()
    for notes in array:
        if personal_notes.personal_notes.get_id(note) == personal_notes.personal_notes.get_id(notes):
            personal_notes.personal_notes.set_id(note)
    array.append(note)
    file_action.write_file(array, 'a')
    print('Заметка добавлена...')


def show(text):
    action = True
    array = file_action.read_file()
    if text == 'date':
        date = input('Введите дату (dd.mm.yyyy): ')
    for notes in array:
        if text == 'all':
            action = False
            print(personal_notes.personal_notes.map_note(notes))
        if text == 'id':
            action = False
            print('ID: ' + personal_notes.personal_notes.get_id(notes))
        if text == 'date':
            action = False
            if date in personal_notes.personal_notes.get_date(notes):
                print(personal_notes.personal_notes.map_note(notes))
    if action == True:
        print('Нет ни одной заметки...')


def id_edit_del_show(text):
    id = input('Введите id заметки: ')
    array = file_action.read_file()
    action = True
    for notes in array:
        if id == personal_notes.personal_notes.get_id(notes):
            action = False
            if text == 'edit':
                note = program.create_note(number)
                personal_notes.personal_notes.set_title(notes, note.get_title())
                personal_notes.personal_notes.set_body(notes, note.get_body())
                personal_notes.personal_notes.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(personal_notes.personal_notes.map_note(notes))
    if action == True:
        print('Такой заметки нет или введен неверный номер id')
    file_action.write_file(array, 'a')