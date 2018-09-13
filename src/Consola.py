import os

# Greeter is a terminal application that greets old friends warmly,
#   and remembers new friends.

### FUNCTIONS ###

def display_title_bar():
    # Clears the terminal screen, and displays a title bar.
    os.system('cls' if os.name == 'nt' else 'clear')

    print("\t**********************************************")
    print("\t***  Greeter - Hello old and new friends!  ***")
    print("\t**********************************************")


def get_user_choice():
    # Let users know what they can do.
    print("\n[1] See a list of friends.")
    print("[2] Tell me about someone new.")
    print("[q] Quit.")

    return input("What would you like to do? ")


def show_names():
    # Shows the names of everyone who is already in the list.
    print("\nHere are the people I know.\n")
    for name in names:
        print(name.title())


def get_new_name():
    # Asks the user for a new name, and stores the name if we don't already
    #  know about this person.
    new_name = input("\nPlease tell me this person's name: ")
    if new_name in names:
        print("\n%s is an old friend! Thank you, though." % new_name.title())
    else:
        names.append(new_name)
        print("\nI'm so happy to know %s!\n" % new_name.title())


if __name__ == '__main__':
    names = []

    choice = ''
    display_title_bar()
    while choice != 'q':

        choice = get_user_choice()

        # Respond to the user's choice.
        display_title_bar()
        if choice == '1':
            show_names()
        elif choice == '2':
            get_new_name()
        elif choice == 'q':
            print("\nThanks for playing. Bye.")
        else:
            print("\nI didn't understand that choice.\n")
