from decorators import input_error

@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name.lower()] = phone
    return "Contact added."

@input_error
def update_contact(args, contacts):
    name, phone = args
    if name.lower() not in contacts:
        return 'There is no such contact to update'
    contacts[name.lower()] = phone
    return "Contact updated."

@input_error
def get_phone(args, contacts):
    return contacts[args[0].lower()]