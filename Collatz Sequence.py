# The Collatz Sequence


def collatz(number):
    """a program that I am just starting to understand."""
    if number % 2 == 0:
        print(number // 2)
        return number // 2

    elif number % 2 == 1:
        result = 3 * number + 1
        print(result)
        return result


num = input("Enter number: ")
while num != 1:
    num = collatz(int(num))