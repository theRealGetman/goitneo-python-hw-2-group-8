from collections import UserDict
from src.utils import PhoneValidationError, handle_error


class Field:
    def __init__(self, value, required=False):
        self.value = value
        self.required = required

    def __str__(self):
        return str(self.value)


class Name(Field):
    def __init__(self, value):
        super().__init__(value, True)


class Phone(Field):
    def __init__(self, value):
        if len(value) != 10:
            raise PhoneValidationError()

        super().__init__(value)

    def __eq__(self, other):
        """Overrides the default implementation"""
        if isinstance(other, Phone):
            return self.value == other.value
        return False


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    @handle_error('Phone already exists.')
    def add_phone(self, phone: str):
        phone = Phone(phone)

        if phone in self.phones:
            raise KeyError()

        self.phones.append(phone)

        print(f'Added phone {phone}')

    @handle_error('Phone doesn`t exist.')
    def remove_phone(self, phone: Phone):
        phone = Phone(phone)

        if phone not in self.phones:
            raise KeyError()

        self.phones.remove(phone)

        print(f'Removed phone {phone}')

    @handle_error('Phone doesn`t exist.')
    def edit_phone(self, old: str, new: str):
        old = Phone(old)
        new = Phone(new)

        if old not in self.phones:
            raise KeyError()

        index = self.phones.index(old)
        self.phones[index] = new

        print(f'Changed phone from {old} to {new}')

    @handle_error('Phone doesn`t exist.')
    def find_phone(self, phone: str) -> Phone:
        phone = Phone(phone)

        if phone not in self.phones:
            raise KeyError()

        index = self.phones.index(phone)

        return self.phones[index]


class AddressBook(UserDict):
    @handle_error('Contact already exists.')
    def add_record(self, record: Record):
        name = record.name.value

        if name in self.data:
            raise KeyError()

        self.data[name] = record
        print(f'Contact {name} added.')

    @handle_error('Contact doesn`t exist.')
    def find(self, name: str) -> Record:
        return self.data[name]

    @handle_error('Contact doesn`t exist.')
    def delete(self, name: str):
        self.data.pop(name)
        print(f'Contact {name} deleted.')
