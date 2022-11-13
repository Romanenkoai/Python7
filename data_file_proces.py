def name_input_f():
    name = input('введите имя файла или оставьте пустым для test_table.csv: ')
    if name == '': return 'test_table.csv'
    else: return name
