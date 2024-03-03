from src.local_storage import contacts_storage
from src.utils import input_error


def hello():
    return 'How can I help you?'


@input_error(
    args_error_label='You need to provide name and phone',
    key_error_label='Contact already exists.',
)
def add_contact(args):
    name, phone = args

    if name in contacts_storage:
        raise KeyError()

    contacts_storage[name] = phone
    return 'Contact added.'


@input_error(
    args_error_label='You need to provide name and phone',
    key_error_label='Contact doesn`t exist.',
)
def change_contact(args):
    name, phone = args

    if name not in contacts_storage:
        raise KeyError()

    contacts_storage[name] = phone
    return 'Contact changed.'


@input_error(
    args_error_label='You need to provide name',
    key_error_label='Contact doesn`t exist.',
)
def show_phone(args):
    name = args[0]
    return contacts_storage[name]


def show_all():
    return '\n'.join([f'{name} - {phone}' for name, phone in contacts_storage.items()])


def close():
    return 'Good bye!'


def invalid_command():
    return 'Invalid command.'
