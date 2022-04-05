 
{% include navigation.html %}


**_Code Snippets From Challenges_**

**Lists/Loops**

```
InfoDb = []
# List with dictionary records placed in a list
InfoDb.append({
    "FirstName": "Divyanshi",
    "LastName": "Suri",
    "Grade": "10th",
    "Classes":["AP Calculus","AP Bio ","CSP","3d Animation", "English"]
})


def print_data(n):
    print(InfoDb[n]["FirstName"], InfoDb[n]["LastName"])  # using comma puts space between values
    print("\t", "Schedule: ", end="")  # \t is a tab indent, end="" make sure no return occurs
    print(", ".join(InfoDb[n]["Classes"]))  # join allows printing a string list with separator
    print()

# Hack 2: InfoDB loops. Print values from the lists using three different ways: for, while, recursion
## hack 2a: def for_loop()
def for_loop():
    for n in range(len(InfoDb)):
        print_data(n)
## hack 2b: def while_loop(0)
def while_loop(n):
    while n < len(InfoDb):
        print_data(n)
        n += 1
    return
## hack 2c : def recursive_loop(0)
def recursive_loop(n):
    if n < len(InfoDb):
        print_data(n)
        recursive_loop(n + 1)
    return # exit condition

def tester():
    print_data(0)
    print_data(1)
    print("For loop")
    for_loop()
    print("While loop")
    while_loop(0)  # requires initial index to start while
    print("Recursive loop")
    recursive_loop(0)  # requires initial index to start recursion

if __name__ == "__main__":
    tester()
  
  
  

```
**Fibbonaci** 

def recur_fibonacci(n):
    if n <= 1:
        return n
    else:
        return(recur_fibonacci(n-1) + recur_fibonacci(n-2))

def tester():
    try:
        num = int(input("How many integers should this sequence be? "))
        if num == 0:
            print("Please enter a positive integer: ")
        else:
            print("Fibonacci Sequence: ")
            for i in range(num):
                print(recur_fibonacci(i))
    except ValueError:
        print("Invalid. Try again: ")

if __name__ == "__main__":
    tester()
 ```
  
**Menu/Submenu**
  
```
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
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

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
 ```
  
 **One Animation (Ice Cream):**
  ```
  import time
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"
def ocean_print():
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    print(OCEAN_COLOR + "  " * 35)

# import funcy
import time
# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"
def ocean_print():
    # print ocean
    print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
    print("\n\n\n\n")
    print(OCEAN_COLOR + "  " * 35)
# print ship with colors and leading spaces
def ship_print(position):
    print(ANSI_HOME_CURSOR)
    print(RESET_COLOR)
    sp = " " * position
    print(sp + "    | |   ")
    print(sp + "     |   ")
    print(SHIP_COLOR, end="")
    print(sp + "    --- ")
    print(sp + "   \____/  ")
    print(RESET_COLOR)
# ship function, iterface into this file
def ship():
    # only need to print ocean once
    ocean_print()
    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2
    # loop purpose is to animate ship sailing
    for position in range(start, distance, step):
        ship_print(position)  # call to function with parameter
        time.sleep(.1)



  ```
  
**Christmas Tree**
  ```
#christmastree
#def christmastree(n):
#or i in range(n):
#for j in range(n-i):
#print(' ', end=' ')
#for k in range(2*i+1):
#print('*',end='*')
#print(' ')

#def trunk(n):
#for i in range(n):
#for j in range(n-1):
#print(' ', end =' ')
#print('* * *')
# Input and Function Call
#row = int(input('Number of rows: '))

#def tester():
#christmastree(row)
#trunk(row)
import time

# terminal print commands
ANSI_CLEAR_SCREEN = u"\u001B[2J"
ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
OCEAN_COLOR = u"\u001B[44m\u001B[2D"
SHIP_COLOR = u"\u001B[32m\u001B[2D"
RESET_COLOR = u"\u001B[0m\u001B[2D"

def tree_print(height):
    print("                *        ")
    print("               * *       ")
    print("              * * *      ")
    print("             * * * *      ")
    print("            * * * * *     ")
    print("           * * * * * *  ")
    print("          * * * * * * *    ")
    print("         * * * * * * * *   ")
    print("        * * * * * * * * *    ")
    print("       * * * * * * * * * *    ")
    print("      * * * * * * * * * * *   ")
    print("     * * * * * * * * * * * *     ")
    print("               ***     ")
    print("               ***   ")
    print("               ***     ")
    print(RESET_COLOR)

def tree():
    # only need to print ocean once


    # loop control variables
    start = 0  # start at zero
    distance = 60  # how many times to repeat
    step = 2  # count by 2

    tree_print(0)
    

  ```
  
  **Math Function (LCM)**
  
  ```
 def lcm(number1, number2): # imperative
    if (number1 > number2):
        max = number1
    else:
        max = number2
        while (True):
            if (max % num1 == 0 and max % num2 == 0):
                break
            max = max + 1
    return max

class LCM:
    def innit (self, num1, num2):
        self.number1 = num1
        self.number2 = num2

    def call(self):
        if self.num1 > self.num2:
            max = self.num1

        else:
            max = self.num
        while (True):
            if (max % self.num1 == 0 and max % self.num2 == 0):
                break
            max = max + 1
        return max


def run():
    num = input("1:OOP or 2:mperitive")
    try:
        if num == '1':
            print("The LCM of 48 and 24 is ", lcm(48,24))
        elif num == '2':
            lcmoop = LCM(48,24)
            print("The LCM of 48 and 24 is ", lcmloop())
    except:
        print("Pick a number choice please!")

if __name__ == "__main__":
    run()
  ```
  
  **Swap**
  ```
  
def swapnumbers():
    a = int(input("Enter a number: "))
    b = int(input("Enter a second number: "))

    print("Before: {0} {1}".format(a, b))
    temp = a
    a = b
    b = temp
    print("After:  {0} {1}".format(a, b))
    
  ```
  
  **Keypad**
  ```
  
def printMatrix():
    matrix = [ [1,2,3],[4,5,6],[7,8,9] ]
    for row in matrix:
        for col in row:
            print(col, end="")
        print()


if __name__ == "__main__":
    printMatrix()
  ```
  
