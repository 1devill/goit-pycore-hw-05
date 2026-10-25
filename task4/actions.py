from decorators import input_error

def parse_input(user_input: str):
    cmd, *args = user_input.split()
    return cmd.strip().lower(), *args


@input_error("add [name] [phone]")
def add_contact(args, contacts):
    name, phone = args
    contacts[name.lower()] = (name, phone)
    return f"Contact '{name}' added."


@input_error("change [name] [new phone]")
def update_contact(args, contacts):
    name, phone = args
    stored_name, _ = contacts[name.lower()]
    contacts[name.lower()] = (stored_name, phone)
    return f"Contact '{stored_name}' updated."


@input_error("phone [name]")
def get_phone(args, contacts):
    (name,) = args
    stored_name, phone = contacts[name.lower()]
    return f"{stored_name}: {phone}"


def show_all(contacts):
    if not contacts:
        return "No contacts saved yet."
    width = max(len(name) for name, _ in contacts.values())
    lines = [f"{name:<{width}} : {phone}" for name, phone in contacts.values()]
    return "\n".join(lines)
