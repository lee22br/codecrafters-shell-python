import sys


def main():
    command = ""

    while (True):
        sys.stdout.write("$ ")
        command = input()
        commands = command.split()
        match commands[0]:
            case "exit":
                exit(0)
            case "echo":
                print(command.removeprefix("echo "))
            case "type":
                type(commands[1])
            case _:
                print(f"{command}: command not found")

def type(command):
    builtins = ["exit","echo","type"]
    if command in builtins:
        print(f"{command} is a shell builtin")
    else:
        print(f"{command}: not found")


if __name__ == "__main__":
    main()
