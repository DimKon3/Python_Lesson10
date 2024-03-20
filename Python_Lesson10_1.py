def add_clinic():
    Name = input("Введите имя питомца: ").split()
    Nam_key = Name[0]
    Vid = input("Введите вид животного: ").split()
    Age = input("Введите возраст питомца {} : ".format(Nam_key))
    Owner = input("Введите имя владельца {} : ".format(Nam_key)).split()
    Vid_value = Vid[0]
    Age_value = int(Age)
    Owner_value = Owner[0]
    vet_clinic[Nam_key] = {"Vid":Vid_value, "Age":Age_value, "Owner":Owner_value}
    print("Питомец добавлен в базу клиники")

def print_one(key,nam_key):
    zn = nam_key['Age']%10
    if (nam_key['Age'] > 4) and (nam_key['Age'] < 21): old = "лет"
    elif zn == 1: old = "год"
    elif zn > 1 and zn < 5: old = "года"
    print(f"Это {nam_key['Vid']} по кличке '{key}'. Возраст питомца: {nam_key['Age']} {old}. Имя владельца: {nam_key['Owner']}")

def search_clinic():
    name = input("Введите имя питомца: ").split()
    nam_key = name[0]
    res = vet_clinic.get(nam_key)
    if res: print_one(nam_key, res)
    else: print("Нет такого питомца в базе клиники!")

def del_clinic():
    name = input("Введите имя питомца: ").split()
    nam_key = name[0]
    res = vet_clinic.get(nam_key)
    if res: 
        del vet_clinic[nam_key]
        print(f"Запись о питомце {nam_key} удалена")
    else: print("Нет такого питомца в базе клиники!")

def print_clinic():
    for key,value in vet_clinic.items():
        print_one(key,value)

help = '''
s - поиск в базе по имени питомца
a - добавление нового животного в базу клиники
d - удаление записи из базы клиники
w - вывод на экран всей базы клиники
q - выход
'''

vet_clinic={}
choice = ""
while choice in ("q", "Q", "й", "Й"):
    choice = input("(h - справка >>>) ")
    if choice in ("a", "ф", "A", "Ф"): add_clinic()
    elif choice in ("w", "W", "ц", "Ц"): print_clinic()
    elif choice in ("s", "S", "ы", "Ы"): search_clinic()
    elif choice in ("d", "D", "в", "В"): del_clinic()
    elif choice in ("h", "H", "р", "Р"): print(help)