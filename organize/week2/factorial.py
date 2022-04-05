class factorial:
    def __call__(self, num):
        last = 1
        for i in range(1, num + 1):
            last = last * i
        return last
factorial = factorial()

def tester():
    numbee = input("Enter a number: ")
    numbee = int(numbee)
    print("Factorial: ",factorial(numbee))

if __name__ == "__main__":
    tester()
