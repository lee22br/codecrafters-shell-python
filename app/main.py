import sys


def main():
    command = ""
    while (True):
        sys.stdout.write("$ ")
        command = input()
        if (command == "exit"):
            return
        if (command.startswith("echo ")):
            print(command.removeprefix("echo "))
        else:
            print(f"{command}: command not found")



if __name__ == "__main__":
    main()