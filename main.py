from week0 import keypad, swap, christmas, ship
from week1 import family, fibonacci
from week2 import factorial, lcm, palindrome


# Two styles are supported to execute abstracted logic
# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
main_menu = [
]

# Works similarly to main_menu

sub_menu_data = [
    ["Matrix", keypad.printMatrix],
    ["InfoDb", family.tester],
]

sub_menu_math = [
    ["Swap", swap.swap0],
    ["Fibonacci", fibonacci.tester],
    ["Factorial", factorial.tester],
    ["LCM", lcm.run],
    ["Palindrome", palindrome.runner]
]

sub_menu_adventure = [
    ["Tree", christmas.tree],
    ["Ship", ship.ship]
]

# Menu banner is typically defined by menu owner
border = "=" * 25
banner = f"\n{border}\nPlease Select An Option\n{border}"


# def menu
# using main_menu list:
# 1. main menu and submenu reference are created [Prompts, Actions]
# 2. menu_list is sent as parameter to menuy.menu function that has logic for menu control
def menu():
    title = "Function Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Data", submenu_data])
    menu_list.append(["Math", submenu_math])
    menu_list.append(["Adventure", submenu_adventure])
    buildMenu(title, menu_list)

def submenu_data():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu_data)

def submenu_math():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu_math)

def submenu_adventure():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu_adventure)

def buildMenu(banner, options):
    # header for menu
    print("\u001b[34m",banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print("\u001b[35m", key, '->', value[0])

    # get user choice
    choice = input("\u001b[36mType your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again


if __name__ == "__main__":
    menu()
