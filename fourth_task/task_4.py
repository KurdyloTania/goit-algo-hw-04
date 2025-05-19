def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return "Error: The 'add' command requires a name and phone number!!!"
    name, phone = args
    if not phone.isdigit() or len(phone) != 10:
        return "Error: You need to enter a 10-digit phone number!!!"
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    if len(args) != 2:
        return "Error: The 'change' command requires a name and phone number!!!"
    name, phone = args
    if name not in contacts:
        return f"Error: Contact '{name}' not found!!!"
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    if len(args) != 1:
        return "Error: The 'phone' command only requires a name!!!"
    name = args[0]
    if name not in contacts:
        return f"Error: Contact '{name}' not found!!!"
    return contacts[name]


def show_all(contacts):
    if not contacts:
        return "There are no contacts!"
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
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
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
