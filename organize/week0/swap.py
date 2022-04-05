def swap0():
    a = input("Enter a number: ")
    b = input("Enter another number: ")
    print("python swap")
    print("original: ", a, b)
    a, b = swap1(a, b)
    print("after: ", a, b)
    print()

def swap1(age1,age2):
    temp = age1
    age1 = age2
    age2 = temp
    print("Swap 1 Result:")
    return age1,age2

#returns numbers lowest to highest
def swap2(a, b):
    if a > b:
        b, a = a, b
    print("Swap 2 Result:")
    return a, b

# returns numbers lowest to highest
def swap3(age1, age2):
    if age1 > age2:
        print ("Swap 3 Result:")
        return(age2, age1)
    else:
        print ("Swap 3 Result:")
        return(age1, age2)
