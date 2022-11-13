from import_proces import import_proces
from export_proces import export_proces


def menu_main():
 
    begin = True
    while begin:
        
        print ('------ \n Введите число для соответствующей задачи или иное для выхода: ')
        print ('   1.\t Импорт файла')
        print ('   2.\t Экспорт в файл')

        program = int(input())
        print ()

        if program == 1:
            data = import_proces()
            if data != []:
                input('Данные импортированы \nЧтобы продолжить, нажмите Enter.')
            else: input(f'Не известный формат \nЧтобы продолжить, нажмите Enter.')

        elif program == 2:
            form = export_proces(data)
            if form != 0:
                input(f'Данные экспортированы в формате {form} \nЧтобы продолжить, нажмите Enter.')
            else: input(f'Не известный формат \nЧтобы продолжить, нажмите Enter.')


        else:
            begin = False

if __name__ == '__main__':
    menu_main()
