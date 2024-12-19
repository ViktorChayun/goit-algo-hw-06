# goit-algo-hw-06
https://www.edu.goit.global/uk/learn/26850204/19951493/19951602/homework

У користувача буде адресна книга або книга контактів. 
* Ця книга контактів містить записи. 
* Кожен запис містить деякий набір полів.

Користувач взаємодіє з книгою контактів
* додаючи, видаляючи та редагуючи записи. 
* Також користувач повинен мати можливість шукати в книзі контактів записи за одним або кількома критеріями (полями).

Про поля також можна сказати
    * вони можуть бути обов'язковими (ім'я) та необов'язковими (телефон або email наприклад). 
    * записи можуть містити декілька полів одного типу (декілька телефонів наприклад).

Користувач повинен мати можливість додавати/видаляти/редагувати поля у будь-якому записі.

Сутності:
    + Field: Базовий клас для полів запису.
    + Name: Клас для зберігання імені контакту. Обов'язкове поле.
    + Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
    + Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
    + AddressBook: Клас для зберігання та управління записами.

1. Клас AddressBook:
    + Має наслідуватись від класу UserDict .
    + Реалізовано метод add_record, який додає запис до self.data. 
        + Записи Record у AddressBook зберігаються як значення у словнику. 
        В якості ключів використовується значення 
            Record.name.value.
    + Реалізовано метод find, який знаходить запис за ім'ям. 
        + На вхід отримує один аргумент - рядок, якій містить ім’я. 
        + Повертає об’єкт Record, або None, якщо запис не знайден.
    + Реалізовано метод delete, який видаляє запис за ім'ям.
    + Реалізовано магічний метод __str__ для красивого виводу об’єкту класу AddressBook.

2. Клас Record:
    + Реалізовано зберігання об'єкта Name в атрибуті name.
    + Реалізовано зберігання списку об'єктів Phone в атрибуті phones.
    + Реалізовано метод для додавання - add_phone
        + На вхід подається рядок, який містить номер телефона.
        + перевірити коректність номеру
        + перевірити що такий номер вже існує
        
    + Реалізовано метод для видалення - remove_phone. 
        + На вхід подається рядок, який містить номер телефона.
    + Реалізовано метод для редагування - edit_phone. 
        + На вхід подається два аргумента - рядки, які містять старий номер телефона та новий. 
        + У разі некоректності вхідних даних метод має завершуватись помилкою ValueError.
    + Реалізовано метод для пошуку об'єктів Phone - find_phone. 
        + На вхід подається рядок, який містить номер телефона. 
        + Метод має повертати або об’єкт Phone, або None.
3. Клас Phone:
    + Реалізовано валідацію номера телефону (має бути перевірка на 10 цифр).
    + Наслідує клас Field. Значення зберігaється в полі value