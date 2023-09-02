from links import *


def print_menu():
    print("Favorite Websites:")
    for i, website in enumerate(favorite_websites.keys()):
        print(f"{i + 1}. {website}")
    print("0. Exit")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (0-4): "))
            if choice < 0 or choice > 4:
                print("Invalid choice. Please try again.")
            else:
                return choice
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    while True:
        print_menu()
        choice = get_user_choice()

        if choice == 0:
            print("Goodbye!")
            break

        websites = list(favorite_websites.values())
        url = websites[choice - 1]
        Firefox(url)

if __name__ == '__main__':
    main()