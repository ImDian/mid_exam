numbers = list(map(int, input().split()))

command = input()

while command != "Finish":
    command_list = command.split()
    action = command_list[0]
    value = int(command_list[1])

    if action == "Add":
        numbers.append(value)

    elif action == "Remove":
        if value in numbers:
            numbers.remove(value)

    elif action == "Replace":
        replacement = int(command_list[2])
        numbers[numbers.index(value)] = replacement

    elif action == "Collapse":
        numbers = [number for number in numbers if number >= value]

    command = input()

print(" ".join(map(str, numbers)))
