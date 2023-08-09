from collections import UserDict


class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    def __init__(self, name, phones):
        self.name = name
        self.phones = [phones]

    def add_phone(self):
        pass

    def delete_phone(self):
        pass

    def change_phone(self):
        pass


class Field:
    pass


class Name:
    value = ''

    def __init__(self, name):
        self.name = name
        self.value = name


class Phone:
    value = ''

    def __init__(self, phone):
        self.phones = phone
        self.value = phone


if __name__ == "__main__":
    name = Name('Bill')
    phone = Phone('1234567890')
    rec = Record(name, phone)
    ab = AddressBook()
    ab.add_record(rec)
    assert isinstance(ab['Bill'], Record)
    assert isinstance(ab['Bill'].name, Name)
    assert isinstance(ab['Bill'].phones, list)
    assert isinstance(ab['Bill'].phones[0], Phone)
    assert ab['Bill'].phones[0].value == '1234567890'
    print('All Ok)')
