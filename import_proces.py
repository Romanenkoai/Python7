from pathlib import Path
from data_file_proces import name_input_f
from from_db import import_from_db
delimeter = 0

def import_from_csv (file_name, delimeter):

    input_data =[]
    with open(file_name, "r") as f:
        for line in f:

            data = []
            end_s = 0

            end_s = line.find('\n', end_s+1)
            line = line [0:end_s]
            data = line.split(delimeter)

            input_data.append (data)
    return input_data
            


def  import_proces():
    file_name = name_input_f()
    file_extension = Path(file_name).suffix

    if file_extension == ".csv":

        delimeter = input('введите делитель для формата .csv: ')
        input_data = import_from_csv(file_name, delimeter)
    
    elif file_extension == ".tsv":
        input_data = import_from_csv(file_name, '\t')
    
    elif file_extension == ".db":
        input_data = import_from_db (file_name)

    else: return []


    print(input_data)
    return input_data

if __name__ == '__main__':
    import_proces ()
