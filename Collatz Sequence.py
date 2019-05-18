# The Collatz Sequence


def collatz(number):
    """An algorithm that no matter what positive number you give, it will return 1."""
    number = int(number)
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result


def ask():
    """A function to ask the user for an integer."""
    num = input("Enter an integer: ")
    while num != 1:
        try:
            num = collatz(num)
        except ValueError:
            print("ONLY INTEGER!!!")
            ask()
            break
    again()


def again():
    """Ask the user if want to try a different integer."""
    a = input("Want to try with another number? YES/NO: ")
    while True:
        if a == 'YES':
            ask()
            # Este 'break era el que me faltaba!!!!!!!!!
            break
        elif a == 'NO':
            break
        else:
            again()


ask()
