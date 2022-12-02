#Отвечает за печать справочника

def read_file():
    with open('data.txt', "r", encoding='utf-8') as file:
        tel = file.read()
    return tel