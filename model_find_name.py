#Отвечает за поиск по имени

def read_file():
    with open('data.txt', "r", encoding='utf-8') as file:
        tel_directory = file.read()
        tel_directory = tel_directory.split("\n")
    return tel_directory

    
def find_name(tel_directory, Name): 
    flag = True
    for str in tel_directory:
        if Name in str:
            print(str)
            flag = False
    return flag
