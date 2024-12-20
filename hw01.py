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
    def __init__(self, value):
        if not self._is_valid(value):
            raise ValueError(f"Incorret phone value: '{value}'")
        super().__init__(value)
    
    def _is_valid(self, value)->bool:
        pattern = r"^\d{10}$"
        return re.match(pattern, value) if value else False

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = [] # список з обєктами класу Phone
        
    def add_phone(self, phone):
        p = Phone(phone)
        # перевірка чи такий номер вже існує, щоб не додавати дубль
        if not self.find_phone(phone):
            self.phones.append(p)
    
    def remove_phone(self, phone):
        value = self.find_phone(phone)
        if value:
            self.phones.remove(value)
    
    def edit_phone(self, old_phone:str, new_phone:str):
        # якщо номеру телефону який хочемо змінити не існує або новий номер некоректно заданий - викликаємо помилку
        if not self.find_phone(old_phone):
            raise ValueError(f"Can't edit. Old phone '{old_phone}' is not found.")        
        # якщо телефон дійсно змінився
        if old_phone !=  new_phone:
            self.add_phone(new_phone)
            self.remove_phone(old_phone)
    
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
        return self.data.get(name)

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
    
    try:
        john_record.add_phone("fdsdfds")    # incorrect value
    except Exception as err:
        print(err)
        
    try:
        john_record.add_phone(None)         # incorrect value
    except Exception as err:
        print(err)
    
    try:
        john_record.add_phone("5555")       # incorrect value
    except Exception as err:
        print(err)
    

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

    jane_record.remove_phone("111111111111") # remove not exiting phone
    try:
        jane_record.edit_phone("2222222222", "33333333333") # new value incorrect
    except Exception as err:
        print(err)
    
    try:
        jane_record.edit_phone("2222222222222", "3333333333") # edit not existing phone
    except Exception as err:
        print(err)
    
    jane_record.edit_phone("2222222222", "3333333333")
    jane_record.edit_phone("3333333333","3333333333")
    try:
        jane_record.edit_phone("3333333333",None)
    except Exception as err:
        print(err)
    print(jane_record)

    # Видалення запису Jane
    book.delete("Jane")
    print(book)
    book.delete("John")
    print(book)
    book.delete("XXXXX")
    
if __name__ == "__main__":
    main()