# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
#  Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные
# Программа должна сохранять данные в текстовом файле
# Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# Использование функций. Ваша программа не должна быть линейной

import os


def add_person():
    last_name = input("Введите фамилию: ")
    name = input("Введите имя: ")
    surname = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    data = open("C:\\Users\\М\\OneDrive\\Рабочий стол\\Python_homework8\\Python_homework8\\Files\\phonebook.txt", "a", encoding="utf-8")
    data.writelines([last_name + " ", name + " ", surname + " ", phone, "\n"])
    data.close()


def print_data():
    with open("C:\\Users\\М\\OneDrive\\Рабочий стол\\Python_homework8\\Python_homework8\\Files\\phonebook.txt", "r", encoding="utf-8") as data:
        print(data.read())


def search():
    search_name = input("Введите данные для поиска: ")
    with open("C:\\Users\\М\\OneDrive\\Рабочий стол\\Python_homework8\\Python_homework8\\Files\\phonebook.txt", "r", encoding="utf-8") as data:
        for line in data:
            if search_name in line:
                print(line)


def load_data():
    with open("C:\\Users\\М\\OneDrive\\Рабочий стол\\Python_homework8\\Python_homework8\\Files\\phonebook.txt", "r+", encoding="utf-8") as data:
        text_data = data.read()
        path = input(
            "Введите путь к файлу, из которого нужно скопировать данные: ")
        with open(path, "r", encoding="utf-8") as data2:
            for line in data2:
                if line not in text_data:
                    data.write(line)
                    
def change_data():
    change_name = input("Введите имя или фамилию абонента, данные которого хотите изменить: ")
    last_name = input('Введите новую фамилию: ')
    name = input('Введите новое имя: ')
    surname = input('Введите новое отчество: ')
    phone = input('Введите новый номер телефона: ')
    with open("C:\\Users\\М\\OneDrive\\Рабочий стол\\Python_homework8\\Python_homework8\\Files\\phonebook.txt", "r", encoding="utf-8") as data:
        list_of_lines = data.readlines()
        for index_line in range(len(list_of_lines)):
            if change_name in list_of_lines[index_line]:
                list_of_lines[index_line] = last_name + ' ' + name + ' ' + surname + ' ' + phone + "\n"
    with open("C:\\Users\\М\\OneDrive\\Рабочий стол\\Python_homework8\\Python_homework8\\Files\\phonebook.txt", "w", encoding="utf-8") as data:
        for line in list_of_lines:
            data.write(line)

def del_data():
    del_name = input('Введите фамилию или имя абонента, данные которого хотите удалить: ')
    with open("C:\\Users\\М\\OneDrive\\Рабочий стол\\Python_homework8\\Python_homework8\\Files\\phonebook.txt", "r", encoding="utf-8") as data:
        list_of_lines = data.readlines()
        for index_line in range(len(list_of_lines)):
            if del_name in list_of_lines[index_line]:
                del list_of_lines[index_line]
                break
    with open("C:\\Users\\М\\OneDrive\\Рабочий стол\\Python_homework8\\Python_homework8\\Files\\phonebook.txt", "w", encoding="utf-8") as data:
        for line in list_of_lines:
            data.write(line)    

 
def ui():
    # os.system("cls")
    print("""1 - Добавить абонента
2 - Поиск абонента
3 - Импорт данных
4 - Вывод списка абонентов
5 - Изменить данные абонента
6 - Удалить абонента
7 - Выход""")
    user_input = input("Введите номер нужного действия: ")
    while user_input != "7":
        if user_input == "1":
            add_person()
        elif user_input == "2":
            search()
        elif user_input == "3":
            load_data()
        elif user_input == "4":
            print_data()
        elif user_input == "5":
            change_data()
        elif user_input == "6":
            del_data()
        else:
            print("Вы ввели некорректный вариант, попробуйте еще раз: ")
        # os.system("cls")
        print("""1 - Добавить абонента
2 - Поиск абонента
3 - Импорт данных
4 - Вывод списка абонентов
5 - Изменить данные абонента
6 - Удалить абонента
7 - Выход""")
        user_input = input("Введите номер нужного действия: ")

def main():
    ui()

if __name__ == "__main__":
    main()


