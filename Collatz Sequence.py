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
    num = input("Enter a number: ")
    while num != 1:
        try:
            num = collatz(num)
        except ValueError:
            print("Just enter a number!")



ask()
