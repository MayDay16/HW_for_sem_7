#Отвечает за создание новой записи

def adding_data(new_entry):
    with open('data.txt', "a", encoding='utf-8') as file:
        file.writelines(new_entry)