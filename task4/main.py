from actions import parse_input, add_contact, update_contact, get_phone

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    intro_text = [
        "Commands are:",
        "1. hello",
        "2. add [ім'я] [номер телефону]",
        "3. change [ім'я] [новий номер телефону]",
        "4. phone [ім'я]",
        "5. all",
        "6. close/exit",
    ]
    print("\n".join(intro_text))

    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(update_contact(args, contacts))
        elif command == "phone":
            print(get_phone(args, contacts))
        elif command == "all":
            print(contacts)
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()