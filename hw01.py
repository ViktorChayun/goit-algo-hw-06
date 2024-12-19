from collections import UserDict
import re

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    pass

class Phone(Field):
    def isValid(self)->bool:
        pattern = r"^\d{10}$"
        return re.match(pattern, self.value) if self.value else False

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = [] # список з обєктами класу Phone
        
    def add_phone(self, phone):
        p = Phone(phone)
        # перевірка на коректінсть формату телефону і чи такий номер вже існує, щоб не додавати дубль
        if p.isValid() and not self.find_phone(phone):
            self.phones.append(p)
    
    def remove_phone(self, phone):
        value = self.find_phone(phone)
        if value:
            self.phones.remove(value)
    
    def edit_phone(self, old_phone:str, new_phone:str):
        found_phone = self.find_phone(old_phone)
        new_p = Phone(new_phone)
        # не знайдено старий номер телефону або новий заданий некоректно        
        if not found_phone or not new_p.isValid():
            raise ValueError        
        # заміна старого телефону новим
        found_phone.value = new_p.value
    
    def find_phone(self, phone:str) -> Phone:
        for p in self.phones:
            if p.value == phone:
                return p
        return None
        
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record:Record):
        # якщо такого запису по імені людини ще не існує, тоді додаємо
        if not self.find(record.name.value):
            self.data[record.name.value] = record
    
    def find(self, name)->Record:
        return self.data[name] if name in self.data else None

    def delete(self, name):
        if self.find(name):
            del self.data[name]
            
    def __str__(self):
        res = "\n".join(str(rec) for rec in self.data.values())
        return res
###############################################################
def main():
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")
    john_record.add_phone("5555555555") # same phone --> issue
    john_record.add_phone("fdsdfds")    # incorrect value
    john_record.add_phone(None)         # incorrect value
    john_record.add_phone("5555")       # incorrect value

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    jane_record.add_phone("1111111111")
    jane_record.add_phone("2222222222")
    book.add_record(jane_record)

    # спроба додати вже існуючу людину
    jane_record2 = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record2)

    # Виведення всіх записів у книзі  
    print(book)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: John: 5555555555

    jane_record.remove_phone("1111111111")
    try:
        jane_record.edit_phone("2222222222", "33333333333") # new value incorrect
    except ValueError:
        print("ValueError: incorrect phone numbe")

    jane_record.edit_phone("2222222222", "3333333333")

    print(jane_record)

    # Видалення запису Jane
    book.delete("Jane")
    print(book)
    book.delete("John")
    print(book)
    book.delete("XXXXX")
    
if __name__ == "__main__":
    main()