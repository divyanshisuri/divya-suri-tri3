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
