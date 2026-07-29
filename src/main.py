from cli.menu import show_menu
from cli.commands import execute


def main():
    while True:
        show_menu()

        choice = input("\nSelect an option: ").strip()

        if choice == "7":
            print("Goodbye!")
            break

        execute(choice)


if __name__ == "__main__":
    main()
