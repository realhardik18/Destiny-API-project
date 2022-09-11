from traceback import print_tb


def returnCommands():
    with open('commands.txt', 'r') as file:
        lines = file.readlines()
        commands = list()
        for command in lines:
            commands.append(command.strip('\n'))
    return commands


# print(returnCommands())
