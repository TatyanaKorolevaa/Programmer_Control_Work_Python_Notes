import functions as func
import program


def run():
    choice = ''
    while choice != '7':
        program.menu()
        choice = input().strip()
        if choice == '1':
            func.show('all')
        if choice == '2':
            func.add()
        if choice == '3':
            func.show('all')
            func.id_edit_del_show('del')
        if choice == '4':
            func.show('all')
            func.id_edit_del_show('edit')
        if choice == '5':
            func.show('date')
        if choice == '6':
            func.show('id')
            func.id_edit_del_show('show')
        if choice == '7':
            break