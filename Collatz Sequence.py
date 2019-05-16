# The Collatz Sequence


def collatz(number):
    """An algorithm that no matter what positive number you give, it will return 1."""
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result


def ask():
    """..."""
    num = int(input("Enter number: "))

    try:
        num

    except ValueError or UnboundLocalError:
        print("Just enter a number!")

    while num != 1:
        num = collatz(num)


ask()
