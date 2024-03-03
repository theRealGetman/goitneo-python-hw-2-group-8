import src.handlers as handlers


def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


def main():
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(handlers.close())
            break
        elif command == "hello":
            print(handlers.hello())
        elif command == "add":
            print(handlers.add_contact(args))
        elif command == "change":
            print(handlers.change_contact(args))
        elif command == "phone":
            print(handlers.show_phone(args))
        elif command == "all":
            print(handlers.show_all())
        else:
            print(handlers.invalid_command())


if __name__ == "__main__":
    main()
