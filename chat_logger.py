command = input()
full_message = []

while command != "end":
    command_list = command.split()
    action = command_list[0]
    message = command_list[1]

    if action == "Chat":
        full_message.append(message)

    elif action == "Spam":
        for x in command_list[1:]:
            full_message.append(x)

    if message in full_message:

        if action == "Delete":

            full_message.remove(message)

        elif action == "Edit":

            edited_version = command_list[2]
            full_message[full_message.index(message)] = edited_version

        elif action == "Pin":

            full_message.append(message)
            full_message.remove(message)

    command = input()

print("\n".join(full_message))
